def secure_hash(s):
    return sum(ord(c) for c in s) % 17

EXPECTED_HASH = 2 

def xor_decrypt(data, key_bytes):
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])

def main():
    user_key = input("Enter decryption key: ").strip()

    if secure_hash(user_key) != EXPECTED_HASH:
        print("Access denied: Invalid hash.")
        return

    try:
        with open("flag.enc", "rb") as f:
            encrypted = f.read()
    except FileNotFoundError:
        print("flag.enc not found.")
        return

    try:
        with open("sol/key.enc", "rb") as f:
            decrypted_key = f.read()
    except FileNotFoundError:
        print("key.enc not found.")
        return
    	
    decrypted_flag = xor_decrypt(encrypted, decrypted_key.strip())

    try:
        print("Decrypted flag:", decrypted_flag.decode())
    except UnicodeDecodeError:
        print("Decryption failed. Wrong key or corrupted data.")

if __name__ == "__main__":
    main()
