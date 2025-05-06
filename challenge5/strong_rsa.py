import random
from sympy import isprime
from Crypto.Util.number import inverse, getPrime, bytes_to_long
import hashlib

p = 13

q = getPrime(512)

n = p * q

e = 65537

phi_n = (p - 1) * (q - 1)

d = inverse(e, phi_n)

message = bytes_to_long(flag.encode())

ciphertext = pow(message, e, n)

def save_challenge():
    with open("public_key.txt", "w") as f:
        f.write(f"n: {n}\ne: {e}\n")
    
    with open("ciphertext.txt", "w") as f:
        f.write(f"ciphertext: {ciphertext}\n")

def main():
    save_challenge()
    print("Challenge created. You can now try to break RSA!")
    print("The encrypted message is saved in ciphertext.txt. Good luck!")

if __name__ == "__main__":
    main()
