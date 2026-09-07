from passlib.hash import sha512_crypt

# File names
hash_file_path = "passwordChallenge.txt" 
wordlist_path = "password.lst"   # John The Ripper dictionary of words to guess

def apply_rules(word):
    """Applies the assignment's specific permutation rules to a base word."""
    if len(word) < 2:
        return []
    
    transformed_base = word[0].lower() + word[1].upper() + word[2:].lower()
    
    return [
        "!" + transformed_base,
        "@" + transformed_base,
        "#" + transformed_base
    ]

def crack_password():
    # 1. Read the target hash from password.txt
    try:
        with open(hash_file_path, 'r', encoding='utf-8') as hf:
            line = hf.read().strip()
            if ":" in line:
                target_hash_full = line.split(":")[1]
            else:
                target_hash_full = line
            print(f"Successfully loaded hash from {hash_file_path}")
            
    except FileNotFoundError:
        print(f"Error: Could not find the hash file '{hash_file_path}'.")
        return

    # 2. Perform the dictionary attack
    print(f"Starting dictionary attack using {wordlist_path}...")
    
    try:
        # errors='ignore' prevents crashes if the dictionary has weird characters
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            # Read all words, ignoring comments in the JTR wordlist
            words = [line.strip() for line in file if not line.startswith("#")]
            total_words = len(words)
            
        print(f"Loaded {total_words} words. Generating combinations...")
        
        for index, base_word in enumerate(words):
            # Print a status update every 100 words so you know it hasn't frozen
            if index > 0 and index % 100 == 0:
                print(f"Progress: {index}/{total_words} base words checked...", end='\r')
                
            candidates = apply_rules(base_word)
            
            for candidate_password in candidates:
                # Compare the candidate to the target hash
                if sha512_crypt.verify(candidate_password, target_hash_full):
                    print("\n\n" + "="*40)
                    print("SUCCESS! Password cracked.")
                    print(f"The password is: {candidate_password}")
                    print(f"Base word used:  {base_word}")
                    print("="*40 + "\n")
                    return
                    
        print("\n\nAttack finished. Password was not found in the dictionary.")
        
    except FileNotFoundError:
        print(f"\nError: Could not find the wordlist file '{wordlist_path}'.")

if __name__ == "__main__":
    crack_password()