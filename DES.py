from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


def des_encrypt(plaintext: str, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC)
    ct = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return cipher.iv + ct


def des_decrypt(ciphertext: bytes, key: bytes) -> str:
    iv = ciphertext[:8]
    ct = ciphertext[8:]

    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ct), DES.block_size)

    return plaintext.decode()


if __name__ == "__main__":
    key = b"8BYTEKEY"
    plaintext = "Hello DES Algorithm!"

    encrypted = des_encrypt(plaintext, key)
    decrypted = des_decrypt(encrypted, key)

    print("DES Encryption Demo")
    print(f"Plaintext  : {plaintext}")
    print(f"Key        : {key}")
    print(f"Ciphertext : {binascii.hexlify(encrypted).decode()}")
    print(f"Decrypted  : {decrypted}")
