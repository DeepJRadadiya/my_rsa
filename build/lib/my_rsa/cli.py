import argparse
from my_rsa.rsa import generate_keys, encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description="My RSA Encryption CLI")
    parser.add_argument("action", choices=["generate", "encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("--message", type=str, help="Message to encrypt/decrypt")
    args = parser.parse_args()

    if args.action == "generate":
        public_key, private_key = generate_keys(bits=32)
        print("Public Key:", public_key)
        print("Private Key:", private_key)
    elif args.action == "encrypt":
        if not args.message:
            print("Error: Please provide a message to encrypt using --message")
            return
        public_key = (65537, 123456789)  # Replace with actual key input or retrieval
        encrypted = encrypt(args.message, public_key)
        print("Ciphertext:", encrypted)
    elif args.action == "decrypt":
        if not args.message:
            print("Error: Please provide ciphertext to decrypt using --message")
            return
        private_key = (123456789, 987654321)  # Replace with actual key input or retrieval
        decrypted = decrypt(eval(args.message), private_key)
        print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
