from ctypes import *

# Load the shared library
lib = CDLL('./kyberk2so.dll')

# Define the byte sizes
kyber512skbytes = 1632
kyber512pkbytes = 800
kyber512ctbytes = 768
kyber768skbytes = 2400
kyber768pkbytes = 1184
kyber768ctbytes = 1088
kyber1024skbytes = 3168
kyber1024pkbytes = 1568
kyber1024ctbytes = 1568
kyberssbytes = 32

# Prepare the functions
lib.KemKeypair512.argtypes = [POINTER(c_char), POINTER(c_char)]
lib.KemEncrypt512.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char)]
lib.KemDecrypt512.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char)]
lib.KemKeypair768.argtypes = [POINTER(c_char), POINTER(c_char)]
lib.KemEncrypt768.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char)]
lib.KemDecrypt768.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char)]
lib.KemKeypair1024.argtypes = [POINTER(c_char), POINTER(c_char)]
lib.KemEncrypt1024.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char)]
lib.KemDecrypt1024.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char)]

def kem_keypair512():
    sk = create_string_buffer(kyber512skbytes)
    pk = create_string_buffer(kyber512pkbytes)
    lib.KemKeypair512(sk, pk)
    return sk.raw, pk.raw

def kem_encrypt512(public_key):
    ct = create_string_buffer(kyber512ctbytes)
    ss = create_string_buffer(kyberssbytes)
    pk = c_char_p(public_key)
    lib.KemEncrypt512(pk, ct, ss)
    return ct.raw, ss.raw

def kem_decrypt512(ciphertext, private_key):
    ss = create_string_buffer(kyberssbytes)
    ct = c_char_p(ciphertext)
    sk = c_char_p(private_key)
    lib.KemDecrypt512(ct, sk, ss)
    return ss.raw

def kem_keypair768():
    sk = create_string_buffer(kyber768skbytes)
    pk = create_string_buffer(kyber768pkbytes)
    lib.KemKeypair768(sk, pk)
    return sk.raw, pk.raw

def kem_encrypt768(public_key):
    ct = create_string_buffer(kyber768ctbytes)
    ss = create_string_buffer(kyberssbytes)
    pk = c_char_p(public_key)
    lib.KemEncrypt768(pk, ct, ss)
    return ct.raw, ss.raw

def kem_decrypt768(ciphertext, private_key):
    ss = create_string_buffer(kyberssbytes)
    ct = c_char_p(ciphertext)
    sk = c_char_p(private_key)
    lib.KemDecrypt768(ct, sk, ss)
    return ss.raw

def kem_keypair1024():
    sk = create_string_buffer(kyber1024skbytes)
    pk = create_string_buffer(kyber1024pkbytes)
    lib.KemKeypair1024(sk, pk)
    return sk.raw, pk.raw

def kem_encrypt1024(public_key):
    ct = create_string_buffer(kyber1024ctbytes)
    ss = create_string_buffer(kyberssbytes)
    pk = c_char_p(public_key)
    lib.KemEncrypt1024(pk, ct, ss)
    return ct.raw, ss.raw

def kem_decrypt1024(ciphertext, private_key):
    ss = create_string_buffer(kyberssbytes)
    ct = c_char_p(ciphertext)
    sk = c_char_p(private_key)
    lib.KemDecrypt1024(ct, sk, ss)
    return ss.raw