import os
import subprocess

def run_cmd(cmd, hide_errors=False):
    """Helper function to run shell commands safely."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0 and not hide_errors:
        print(f"  -> ERROR running command: {cmd}")
        if result.stderr:
            print(f"  -> {result.stderr.strip()}")
        if result.stdout:
            print(f"  -> {result.stdout.strip()}")
        return False
    return True

def main():
    print("Initiating Autonomous Mission Solver...\n")

    # --- Step A: Find the file with a valid signature ---
    print("[Step A] Running diagnostics to find the valid file...")
    good_file = None
    
    for i in range(10):
        msg_file = f"message{i}.txt"
        sig_file = f"{msg_file}.sign"
        
        cmd = f"openssl dgst -sha3-256 -verify lab4_public.pem -signature {sig_file} {msg_file}"
        
        # We use subprocess directly here so we can parse the exact text output
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout.strip() + result.stderr.strip()
        
        if result.returncode == 0 or "OK" in output:
            print(f"  -> SUCCESS: {msg_file} verified OK!")
            good_file = msg_file
            break

    if not good_file:
        print("  -> ERROR: Could not find any file with a valid signature. Mission aborted.")
        return

    # --- Step B: Create a text file with the content and my ID ---
    print(f"\n[Step B] Reading {good_file} and appending the ID to answer.txt...")
    try:
        with open(good_file, 'r') as f:
            original_content = f.read()
        
        with open("answer.txt", "w") as f:
            f.write(original_content)
            if not original_content.endswith('\n'):
                f.write('\n')
            f.write("329245161\n")
        print("  -> SUCCESS: answer.txt created.")
    except FileNotFoundError:
        print(f"  -> ERROR: Cannot find {good_file}. Make sure you are in the right directory.")
        return

    # --- Step C: Create an RSA public-private key pair ---
    print("\n[Step C] Generating YOUR 2048-bit RSA key pair...")
    if run_cmd("openssl genrsa -out my_private.pem 2048"):
        run_cmd("openssl rsa -in my_private.pem -pubout -out my_public.pem")
        print("  -> SUCCESS: my_private.pem and my_public.pem generated.")

    # --- Step D: Encrypt the file using lab4_public.pem ---
    print("\n[Step D] Encrypting answer.txt with instructor's public key...")
    encrypt_cmd = "openssl pkeyutl -encrypt -in answer.txt -pubin -inkey lab4_public.pem -out answer.enc"
    if run_cmd(encrypt_cmd):
        print("  -> SUCCESS: answer.enc created.")

    # --- Step E: Sign the file using MY private RSA key ---
    print("\n[Step E] Signing the encrypted file with your private key...")
    sign_cmd = "openssl dgst -sha3-256 -sign my_private.pem -out answer.enc.sign answer.enc"
    if run_cmd(sign_cmd):
        print("  -> SUCCESS: answer.enc.sign created.")

    print("\nMission Complete! 🎯")

if __name__ == "__main__":
    main()