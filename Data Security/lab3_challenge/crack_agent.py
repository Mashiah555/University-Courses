import urllib.request
import json
import hashlib
import binascii
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# The intercepted message
ciphertext_hex = '64c2cf8df2c66bf39754f1498432ee1fe819267e9d15d47543a96fa49b75b103'
ciphertext = binascii.unhexlify(ciphertext_hex)

def get_mitre_names():
    print("Fetching the latest MITRE ATT&CK database...")
    # Official MITRE CTI GitHub raw JSON
    url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
    
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read())
    except Exception as e:
        print(f"Failed to fetch MITRE data: {e}")
        return []

    names = set()
    # Extract both campaigns and threat groups
    for obj in data.get('objects', []):
        if obj.get('type') in ['campaign', 'intrusion-set']:
            raw_name = obj.get('name', '')
            if raw_name:
                # Rule: CAPITAL LETTERS WITH SPACES REMOVED
                formatted = raw_name.replace(" ", "").upper()
                names.add(formatted.encode('utf-8'))
                
    return names

def main():
    candidates = get_mitre_names()
    print(f"Loaded {len(candidates)} candidate campaigns/groups from MITRE.")
    print("Commencing brute-force attack...\n")

    for name in candidates:
        # Step 1: name + name's reverse + '2026'
        payload = name + name[::-1] + b'2026'
        
        # Step 2: First 32 bytes of SHA512
        key = hashlib.sha512(payload).digest()[:32]
        
        # Step 3: Decrypt using AES-ECB
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_raw = cipher.decrypt(ciphertext)
        
        # Step 4: Validate if the output is readable (check the first block to ignore trailing padding bytes)
        printable = set(string.printable.encode('ascii'))
        if all(b in printable for b in decrypted_raw[:16]):
            
            # Clean up the output by removing standard PKCS7 padding if it exists
            try:
                clean_text = unpad(decrypted_raw, AES.block_size).decode('utf-8')
            except ValueError:
                # If unpad fails, just decode ignoring weird trailing bytes
                clean_text = decrypted_raw.decode('utf-8', errors='ignore')
                
            print("="*60)
            print("--- ENEMY MESSAGE DECRYPTED ---")
            print("="*60)
            print(f"Target Campaign/Group : {name.decode('utf-8')}")
            print(f"Derived Key (Hex)     : {binascii.hexlify(key).decode('utf-8')}")
            print(f"Secret Message        : {clean_text}")
            print("="*60)
            return

    print("Brute-force failed. The campaign name might not be in the current MITRE dataset, or it uses an alias.")

if __name__ == '__main__':
    main()