import argparse
import pikepdf
from tqdm import tqdm

def decrypt_pdf_with_password_list(passwords_file, pdf_file):
    # Load password list
    passwords = [line.strip() for line in open(passwords_file)]

    # Iterate over passwords
    for password in tqdm(passwords, "Decrypting PDF"):
        try:
            # Open PDF file
            with pikepdf.open(pdf_file, password=password) as pdf:
                # Password decrypted successfully, break out of the loop
                print("[+] Password found:", password)
                break
        except pikepdf._core.PasswordError as e:
            # Wrong password, continue to the next password
            continue

    print("[-] Password not found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Password Decrypter")
    parser.add_argument("passwords_file", help="Path to the passwords file")
    parser.add_argument("pdf_file", help="Path to the protected PDF file")
    args = parser.parse_args()

    decrypt_pdf_with_password_list(args.passwords_file, args.pdf_file)

##usage in command line
##python pdf_dictionary_attack.py passwords.txt protected.pdf
