from kyberk2so import kem_keypair512, kem_encrypt512, kem_decrypt512
import numpy as np
import secrets
import blake3

context = 'StreamCrypt-2db12ea77123cf47d288753b12914f61102d92a8b3a2d220c65e80a99004f3a7-by-afkaf'


# STREAMCRYPT ENCRYPTION STUFF
# Stream Cipher Encryption using BLAKE3 for key derivation and encryption. Salts are used in place of nonce.
def encrypt_sc(data, keyword):
    salt = secrets.token_bytes(64)  # salt generation
    initial_key = blake3.blake3(keyword + salt, derive_key_context=context).digest(length=64)  # Hash password and salt
    keystream = blake3.blake3(initial_key, derive_key_context=context).digest(length=len(data))
    data_array = np.frombuffer(data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    secret = np.bitwise_xor(data_array, keystream_array).tobytes()
    return salt + secret  # Prepend salt to secret for decryption

def decrypt_sc(secret, keyword):
    salt, encrypted_data = secret[:64], secret[64:]  # Extract salt and encrypted data
    initial_key = blake3.blake3(keyword + salt, derive_key_context=context).digest(length=64)  # Recreate initial key
    keystream = blake3.blake3(initial_key, derive_key_context=context).digest(length=len(encrypted_data))
    encrypted_array = np.frombuffer(encrypted_data, dtype=np.uint8)
    keystream_array = np.frombuffer(keystream, dtype=np.uint8)
    data = np.bitwise_xor(encrypted_array, keystream_array).tobytes()
    return data


# KYBER ENCRYPTION STUFF
# Module lattice based cryptography layer for asymmetric encryption. Uses Kyber512 for key exchange.
def encrypt_k512(data, public_key):
    ct, ss_a = kem_encrypt512(public_key)
    encrypted_data = encrypt_sc(data, ss_a)
    return (encrypted_data, ct)

def decrypt_k512(data, private_key):
    (encrypted_data, ct) = data
    ss_b = kem_decrypt512(ct, private_key)
    decrypted_data = decrypt_sc(encrypted_data, ss_b)
    return decrypted_data


#  MAIN ENCRYPT/DECRYPT
#  High-level encryption/decryption and key creation interface.
def create_keypair():
    return kem_keypair512()

def encrypt(data, public_key):
    return encrypt_k512(data, public_key)

def decrypt(data, private_key):
    return decrypt_k512(data, private_key)


# Example Usage
if __name__ == '__main__':
    private_key, public_key = create_keypair()

    data = b'test data'

    encrypted_data = encrypt(data, public_key)

    decrypted_data = decrypt(encrypted_data, private_key)