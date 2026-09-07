import hashlib

# The target data from the CTF challenge
target_hash = "cbd7163c8dc7d19ed3bcb155dd75d7bd"
salt = "7729"
wordlist_path = "words.txt"

def crack():
    print(f"Starting MD5 brute force using {wordlist_path}...")
    
    try:
        # Open the dictionary file
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                word = line.strip()
                
                # Recreate the hashing logic from the assignment: word + salt
                string_to_hash = word + salt
                encoded_string = string_to_hash.encode('utf-8')
                attempt_hash = hashlib.md5(encoded_string).hexdigest()
                
                # Compare our generated hash to the CTF target
                if attempt_hash == target_hash:
                    print("\n" + "="*45)
                    print("SUCCESS! Password cracked.")
                    print(f"The base dictionary word is: {word}")
                    print(f"The full original string was: {string_to_hash}")
                    print("="*45 + "\n")
                    return
                    
        print("\nAttack finished. Password not found in the dictionary.")
        
    except FileNotFoundError:
        print(f"\nError: Could not find the wordlist file '{wordlist_path}'.")

if __name__ == "__main__":
    crack()