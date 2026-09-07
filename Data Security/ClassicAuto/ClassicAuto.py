# Script to solve challenge #2 - Classic Auto, for exercise 2 question 5
# This script performs frequency analysis on a given ciphertext,
# and allows the user to iteratively build a substitution dictionary to decrypt the text.

import os
import collections
import string

# Standard English letter frequencies (approximate percentages)
ENGLISH_FREQS = {
    'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7, 's': 6.3,
    'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8, 'u': 2.8, 'm': 2.4,
    'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5, 'v': 1.0,
    'k': 0.8, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07
}

def analyze_frequency(ciphertext):
    """Counts the frequency of each letter in the ciphertext."""
    text = ciphertext.lower()
    counts = collections.Counter(c for c in text if c in string.ascii_lowercase)
    total_letters = sum(counts.values())
    
    frequencies = {}
    if total_letters > 0:
        for char, count in counts.items():
            frequencies[char] = (count / total_letters) * 100
            
    # Sort by frequency descending
    return sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

def apply_mapping(ciphertext, mapping_dict):
    """Decrypts the text using a provided dictionary mapping."""
    plaintext = ''
    for char in ciphertext:
        is_upper = char.isupper()
        lower_char = char.lower()
        
        if lower_char in mapping_dict:
            decrypted_char = mapping_dict[lower_char]
            plaintext += decrypted_char.upper() if is_upper else decrypted_char
        else:
            # If not mapped yet, leave it as is (or replace with a placeholder)
            plaintext += char 
    return plaintext

def print_analysis(cipher_freqs):
    print("\n--- Frequency Analysis ---")
    print("\n (Top 5 Expected English Letters: E, T, A, O, I)")
    print(f"{'Cipher Letter':<15} | {'Cipher Freq %':<15}")
    print("-" * 65)
    for char, freq in cipher_freqs:
        print(f"{char.upper():<15} | {freq:<15.2f}")
    print("-" * 65)

if __name__ == "__main__":
    file_path = input("Enter absolute path to the ciphered .txt file: ")
    
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            ciphertext = f.read()
            
        # 1. Analyze and print frequencies
        cipher_freqs = analyze_frequency(ciphertext)
        print_analysis(cipher_freqs)
        
        # 2. Iterative decryption loop
        print("\n--- Building the substitution dictionary ---")
        print("Format your input as: cipher_letter=plain_letter (e.g., x=e). Type 'quit' to exit.")
        
        current_mapping = {}
        
        while True:
            # Show a snippet of the text with the current mapping applied
            preview = apply_mapping(ciphertext[:500], current_mapping)
            print("\n--- Current Decryption Preview ---")
            print(preview)
            print("----------------------------------\n")
            
            user_input = input("Enter mapping (or 'quit'): ").strip().lower()
            if user_input == 'quit':
                break
                
            if '=' in user_input and len(user_input) == 3:
                cipher_char, plain_char = user_input.split('=')
                if cipher_char in string.ascii_lowercase and plain_char in string.ascii_lowercase:
                    current_mapping[cipher_char] = plain_char
                    print(f"Added mapping: {cipher_char.upper()} -> {plain_char.upper()}")
                else:
                    print("Invalid characters. Please use letters only.")
            else:
                print("Invalid format. Use cipher=plain (e.g., x=e).")
                
        # 3. Save the final result if requested
        save = input("Do you want to save the current output? (y/n): ").lower()
        if save == 'y':
            final_text = apply_mapping(ciphertext, current_mapping)
            output_path = os.path.join(os.path.dirname(file_path), 'substitution_deciphered.txt')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_text)
            print(f"Saved to: {output_path}")
            
    else:
        print("File not found.")