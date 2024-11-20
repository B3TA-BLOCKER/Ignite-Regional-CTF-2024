from binascii import unhexlify, hexlify

# Example ciphertexts from interaction (replace with real data from your interaction)
ciphertext_known_input = unhexlify("2d41f1c0b5ce03e3153012564620b710") #replace cipher
flag_ciphertext = unhexlify("1e37e6053e360e899678aa51b6443786d703b87d24d72e99847fbe5e268d115081dd0a5307602a455d8a4c149dc95a8b894d1c14c9bdfeccef8dfe79cbabb25a783e719437cbb800a4b5fd5f312e28ea263f9c9fea915cbc4a6f4d09197fd17c4c268af3d0fe35d522002b6f701287294c2793f885ac358071512433234282721f22c6a182fa32812406216e7314d6721f2097f781fb3787740271637e1280211d71c6f182fd32d420022b62724ce37b412a97f2dbfa62862700276f7317d3271827c8f081aa658076092b6e244384221a72c8f487fb308621062161707f86281a708c9fea915cbc4a6f4d09197fc178d556ab86818287761cefdf496b9dc2795cee0fbdcbcafe19488ae7e63505f31e49fca58f8acc016b6c4d1f352a363d05158ea999d3b0f553f4123de6373f9aedeceaef625bfa84fe58a21c9e2671b0001e")  # replace cypher

# Known plaintext input (all zero block, for simplicity)
known_plaintext = bytes([0] * 16)

# Derive keystream by XORing known plaintext with its ciphertext
keystream = bytes([pt ^ ct for pt, ct in zip(known_plaintext, ciphertext_known_input)])

# Decrypt the flag by XORing the keystream with the flag ciphertext block by block
flag_plaintext = b""
for i in range(0, len(flag_ciphertext), 16):
    flag_block = flag_ciphertext[i:i+16]
    decrypted_block = bytes([ks ^ fb for ks, fb in zip(keystream, flag_block)])
    flag_plaintext += decrypted_block

print("Decrypted flag:", flag_plaintext.decode(errors='ignore'))
