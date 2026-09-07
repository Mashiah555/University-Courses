# Script to solve challenge #1 - Read The Manual, for exercise 2 question 4
# This script will take a ciphertext input and attempt to decrypt it using all possible Caesar cipher shifts (0-25).
# The user can then review the possible decryptions to identify the correct one. 
# Once the correct shift is identified, the script can be used to decrypt a .txt file containing the ciphered text and save the output to a new file.

import os

def get_all_offsets(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    possible_plaintexts = {}

    for shift in range(26):
        plaintext = ''
        for char in ciphertext.lower():
            if char in alphabet:
                original_index = alphabet.find(char)
                decrypted_index = (original_index - shift) % 26
                plaintext += alphabet[decrypted_index]
            else:
                plaintext += char
        possible_plaintexts[shift] = plaintext
    return possible_plaintexts

def caesar_decrypt(ciphertext, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    for char in ciphertext.lower():
        if char in alphabet:
            original_index = alphabet.find(char)
            decrypted_index = (original_index - shift) % 26
            plaintext += alphabet[decrypted_index]
        else:
            plaintext += char
    return plaintext

def print_all_possible_decryptions(decryptions):
    print("Possible Caesar cipher decryptions (unknown offset):\n")
    for shift, plaintext in decryptions.items():
        print(f"Shift of {shift:2}:\n{plaintext}")
    print("\nTo find the correct decryption, look for the most readable and meaningful text.\n")

if __name__ == "__main__":
    ciphertext = input("Enter a snippet of the ciphertext to decrypt: ")
    possible_decryptions = get_all_offsets(ciphertext)
    print_all_possible_decryptions(possible_decryptions)

    try:
        shift = int(input("\nEnter the correct shift number (0-25): "))
        if 0 <= shift <= 25:
            file_path = input("Enter absolute path to the ciphered .txt file: ")
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                decrypted = caesar_decrypt(content, shift)

                output_path = os.path.join(os.path.dirname(file_path), 'deciphered_output.txt')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted)

                print(f"Decrypted text saved to: {output_path}")
            else:
                print("File not found.")
        else:
            print("Invalid shift. Must be between 0 and 25.")
    except ValueError:
        print("Invalid input. Shift must be an integer.")
