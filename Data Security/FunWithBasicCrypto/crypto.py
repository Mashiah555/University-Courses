import hashlib
import base64
import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def try_decrypt_raw(key, iv, ciphertext):
    # Decrypt without any padding checks
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def is_readable_text(byte_data):
    # Check if the decrypted bytes look like standard ASCII text (letters, numbers, basic punctuation)
    allowed_chars = set(string.ascii_letters.encode('ascii') + 
                        string.digits.encode('ascii') + 
                        b"{}_-!@? /.")
    
    printable_count = sum(1 for b in byte_data if b in allowed_chars)
    # If at least 12 out of 16 bytes are normal text, it's a very strong candidate
    return printable_count >= 12

if __name__ == "__main__":
    text_file_path = input("Enter the path to the original text file: ")
    encrypted_file_path = input("Enter the path to the encrypted file: ")
    # text_file_path = r"C:\PythonScripts\FunWithBasicCrypto\file.txt"
    # encrypted_file_path = r"C:\PythonScripts\FunWithBasicCrypto\secret.txt"

    with open(encrypted_file_path, 'r', encoding='utf-8') as f:
        ciphertext = base64.b64decode(f.read().strip())

    # Read the raw file
    with open(text_file_path, 'rb') as f:
        raw_binary = f.read()

    algos = ['md5', 'sha1', 'sha256', 'sha512']
    found = False

    for algo in algos:
        h = hashlib.new(algo)
        h.update(raw_binary)
        full_digest = h.digest()
        
        # Method 1: Raw Bytes
        key_raw = full_digest[:16]
        decrypted_raw = try_decrypt_raw(key_raw, key_raw, ciphertext)
        
        if is_readable_text(decrypted_raw):
            print("="*50)
            print(f"🎉 POTENTIAL MATCH FOUND! (Algo: {algo.upper()})")
            # We ignore decode errors in case there are trailing null bytes
            print(f"Decrypted text: {decrypted_raw.decode('ascii', errors='ignore')}")
            print("="*50)
            found = True

        # Method 2: Hex Bytes
        hex_digest = h.hexdigest().encode('utf-8')
        key_hex = hex_digest[:16]
        decrypted_hex = try_decrypt_raw(key_hex, key_hex, ciphertext)
        
        if is_readable_text(decrypted_hex):
            print("="*50)
            print(f"🎉 POTENTIAL MATCH FOUND! (Algo: {algo.upper()} - HEX KEY) 🎉")
            print(f"Decrypted text: {decrypted_hex.decode('ascii', errors='ignore')}")
            print("="*50)
            found = True

    if not found:
        print("No readable text found, there must be an issue with the key derivation or the ciphertext.")