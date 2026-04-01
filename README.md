SipHash + Affine Cipher + Authentication Type A

SipHash - Hash Function:

- SipHash is a keyed hash function,it uses two secret keys (key1, key2) to generate a secure hash.
- It initializes four internal variables using constants and keys, which helps in creating randomness.
- The message is processed character by character using a mixing function called sipround, which spreads the influence of each character across all variables.
- After several rounds of mixing, the final hash is produced by XOR-ing all internal variables, giving a 64-bit hash value.

Affine Cipher (Encryption & Decryption):

Encryption is done using:
            E(x) = (a(x) + b) mod 62
- Here a = 5 and b = 8, where each character is converted to a number (Base62), transformed, and converted back.

Decryption is done using:
            D(x) = (a^-1(x) - b) mod 62
- where a^-1 is modular inverse of a.

Authentication Type A:

- The hash of the message is first generated using a hash function (SipHash).
- This hash is then concatenated with the original message to form a combined data.
- The combined data is encrypted using the affine cipher before transmission.
- At the receiver side, the data is decrypted, split into hash and message, and the hash is recomputed.
- If both hashes match, the message is authentication successful otherwise authentication unsuccessful.


Instructions to Run:
- Clone the repository
- Open terminal and navigate to the project folder
- Run the file : python cia.py
- Enter the plaintext message
- View the hash, encrypted output, decrypted value, and authentication result

