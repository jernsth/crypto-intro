# Schlüssel und Flagge
key = "verysecurekey".encode()
flag = "flag{c0llisi0n_d3tect1on_successful}".encode()

# XOR-Verschlüsselung
def xor_encrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Verschlüsselung der Flagge
encrypted_flag = xor_encrypt(flag, key)

# Ausgabe der verschlüsselten Flagge als Hex
print(encrypted_flag.hex())

# Speichern der verschlüsselten Flagge als Datei
with open("flag.enc", "wb") as f:
    f.write(encrypted_flag)
