from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
 
# Get rand key
AES_key = 8 * get_random_bytes(2)
print(AES_key)