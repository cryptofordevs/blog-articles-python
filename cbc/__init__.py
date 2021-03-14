from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

# initialize IV and key
IV = get_random_bytes(16)
key = get_random_bytes(16)

# init AES in CBC mode
aes = AES.new(key, AES.MODE_CBC, IV)

# plaintext
plaintext = bytearray("0000000000000000", 'utf-8')

# encrypt
ciphertext = aes.encrypt(plaintext)

print(ciphertext)