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


# Usage example
decrypt_pdf_with_password_list("passwords.txt", "protected.pdf")
