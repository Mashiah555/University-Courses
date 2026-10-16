from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine, load_digits

def analyze_full_tree(dataset):
    """
    Analyzes a given dataset using a full Decision Tree Classifier.
    
    This function extracts features and targets, splits the data into
    training and testing sets, trains a Decision Tree using the 'entropy'
    criterion with no depth limit, and evaluates its performance.
    
    Args:
        dataset: A dataset object (e.g., from sklearn.datasets) containing 
                 'data' and 'target' attributes.
                 
    Returns:
        tuple: (max_depth, X_train, X_test, y_train, y_test)
    """
    
    # Extract features (X) and target (y)
    X = dataset.data
    y = dataset.target
    
    # Split the dataset into training and testing sets (30% test size, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize the Decision Tree Classifier with 'entropy' criterion and no depth limit
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=None, random_state=42)
    
    # Train the model on the training data
    clf.fit(X_train, y_train)
    
    # Retrieve the maximum depth of the resulting tree
    max_depth = clf.get_depth()
    
    # Generate predictions using the test set
    y_pred = clf.predict(X_test)
    
    # Calculate performance metrics using 'weighted' average for multiclass support
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    # Print the calculated metrics and tree details
    print(f"Maximum Tree Depth: {max_depth}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision (Weighted): {precision:.4f}")
    print(f"Recall (Weighted): {recall:.4f}")
    print(f"F1-Score (Weighted): {f1:.4f}")
    
    # Return the maximum depth along with the split datasets
    return max_depth, X_train, X_test, y_train, y_test

def evaluate_depths_table(X_train, X_test, y_train, y_test, max_depth):
    """
    Evaluates Decision Trees at various depths and compiles the performance metrics.
    
    This function iterates through tree depths from 1 up to the specified max_depth.
    For each depth, it trains a DecisionTreeClassifier using the 'entropy' criterion, 
    evaluates its predictions on the test set, and stores the accuracy, precision, 
    recall, and F1-score in a pandas DataFrame.
    
    Args:
        X_train: Training features.
        X_test: Testing features.
        y_train: Training targets.
        y_test: Testing targets.
        max_depth: The maximum tree depth to evaluate (integer).
        
    Returns:
        pandas.DataFrame: A DataFrame containing the performance metrics for each depth.
    """
    
    # List to hold the evaluation metrics for each depth
    evaluation_results = []
    
    # Loop through depths from 1 to max_depth (inclusive)
    for depth in range(1, max_depth + 1):
        # Initialize the model for the current depth
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=depth, random_state=42)
        
        # Train the model
        clf.fit(X_train, y_train)
        
        # Generate predictions
        y_pred = clf.predict(X_test)
        
        # Calculate metrics using 'weighted' average
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        
        # Store the metrics in a dictionary
        evaluation_results.append({
            'Depth': depth,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        })
        
    # Convert the list of dictionaries into a pandas DataFrame
    results_df = pd.DataFrame(evaluation_results)
    
    # Print the DataFrame as a formatted table (excluding the row indices for clarity)
    print("Decision Tree Performance by Depth:")
    print("-" * 65)
    print(results_df.to_string(index=False, float_format="%.4f"))
    print("-" * 65)
    
    # Return the DataFrame for further use
    return results_df

def plot_metrics_vs_depth(metrics_df, dataset_name):
    """
    Plots evaluation metrics (Accuracy, Precision, Recall, F1-Score) against decision tree depth.
    
    This function visualizes how different performance metrics change as the depth
    of the decision tree increases, helping to identify potential overfitting or underfitting.
    
    Args:
        metrics_df (pandas.DataFrame): DataFrame containing 'Depth' and the corresponding 
                                       evaluation metrics.
        dataset_name (str): The name of the dataset, used to customize the plot title.
    """
    
    # Initialize the figure with a clear size
    plt.figure(figsize=(10, 6))
    
    # Extract the x-axis values (Tree Depth)
    depths = metrics_df['Depth']
    
    # Plot each metric as a function of depth, using distinct markers for clarity
    plt.plot(depths, metrics_df['Accuracy'], marker='o', label='Accuracy')
    plt.plot(depths, metrics_df['Precision'], marker='s', label='Precision')
    plt.plot(depths, metrics_df['Recall'], marker='^', label='Recall')
    plt.plot(depths, metrics_df['F1-Score'], marker='d', label='F1-Score')
    
    # Add title and axis labels
    plt.title(f"Decision Tree Performance Metrics vs. Depth ({dataset_name})", fontsize=14, fontweight='bold')
    plt.xlabel("Maximum Tree Depth", fontsize=12)
    plt.ylabel("Score (0.0 to 1.0)", fontsize=12)
    
    # Ensure the x-axis ticks align exactly with the integer depths evaluated
    plt.xticks(depths)
    
    # Enable the grid to make it easier to read specific values
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add a legend to identify the plotted lines
    plt.legend(loc='best')
    
    # Adjust layout to prevent clipping and display the plot
    plt.tight_layout()
    plt.show(block=False)
    print(f"--- Opened {dataset_name} Graph ---")

# =========================================================
# Main Execution
# =========================================================
if __name__ == "__main__":
    # Define the datasets to process
    datasets = [
        (load_iris, "Iris"),
        (load_wine, "Wine"), 
        (load_digits, "Digits") 
    ]
    best_depths_info = []

    # Iterate through all datasets
    for dataset_func, name in datasets:
        print(f"\n{'='*50}")
        print(f"Analyzing Dataset: {name}")
        print(f"{'='*50}")
        
        # Load the current dataset
        dataset = dataset_func()
        
        # Train full tree to get splits and maximum depth
        max_depth, X_train, X_test, y_train, y_test = analyze_full_tree(dataset)
        
        # Evaluate all depths up to max_depth and generate the metrics table
        metrics_df = evaluate_depths_table(X_train, X_test, y_train, y_test, max_depth)
        
        # Plot the metrics vs. depth for graphic analysis
        plot_metrics_vs_depth(metrics_df, name)
        
        # Find the best depth for accuracy to store for the summary
        best_index = metrics_df['Accuracy'].idxmax()
        best_depth = int(metrics_df.loc[best_index, 'Depth'])
        best_accuracy = metrics_df.loc[best_index, 'Accuracy']
        
        # Store the summary info
        best_depths_info.append((name, best_depth, best_accuracy))

    # Print the best depth for accuracy for each dataset
    print("\nSUMMARY: Best Tree Depth for Accuracy")
    print("="*50)
    for name, depth, accuracy in best_depths_info:
        print(f"Dataset: {name:<10} | Best Depth: {depth:<2} | Accuracy: {accuracy:.4f}")

    # Wait for user input to prevent the program termination
    print("\n" + "-"*50)
    print("Press any key to exit and dismiss the graphs...")
    input()