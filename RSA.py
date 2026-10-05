from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def gcd(a, b):
    while b: a, b=b, a%b
    return a

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0: return a, 1, 0
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a//b) * y
    _, x, _ = extended_gcd(e, phi)
    return x % phi

def rsa_manual(p=61, q=53):
    n    = p * q
    phi  = (p - 1) * (q - 1)
    e    = 17
    assert gcd(e, phi) == 1
    d    = mod_inverse(e, n)
    msg  = 65
    C    = pow(msg, e, n)
    M    = pow(C, d, n)
    print(f"  p={p}, q={q}, n={n}, phi={phi}")
    print(f"  Public Key  (e={e}, n={n})")
    print(f"  Private Key (d={d}, n={n})")
    print(f"  Message={msg}  Ciphertext={C}  Decrypted={M}")

def rsa_library():
    key = RSA.generate(2048)
    pub_key = key.publickey()

    cipher = PKCS1_OAEP.new(pub_key)

    msg = b"RSA Encryption Test - SCSVMV"
    ct = cipher.encrypt(msg)

    dec_cipher = PKCS1_OAEP.new(key)
    pt = dec_cipher.decrypt(ct)

    print(f"Original  : {msg.decode()}")
    print(f"Encrypted : {binascii.hexlify(ct)[:40].decode()}...")
    print(f"Decrypted : {pt.decode()}")

print("=== Manual RSA (p=61, q=53) ===")
rsa_manual()

print("\n=== RSA with 2048-bit keys (Library) ===")
rsa_library()
