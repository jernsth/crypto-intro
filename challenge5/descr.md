# Weak RSA

We intercepted a message that was encrypted using RSA.  
However, our analysts noticed something odd: one of the prime numbers used in the key generation process seems to be way too small.

**Can you break RSA when one of the prime factors is known?**

You are given:
- `public_key.txt` containing `n` and `e`
- `ciphertext.txt` containing the RSA-encrypted message

Your task is to recover the original flag.

**Hint:**  
Remember how RSA works — if you know _one_ of the prime factors, you can break the rest.
