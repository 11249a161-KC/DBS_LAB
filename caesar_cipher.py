def caesar_cipher(text, shift, mode='encrypt'):
    result=""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char

    return result
if __name__ == "__main__":
    message = "Hello, World!"
    key = 3

    encrypted = caesar_cipher(message, key, mode='encrypt')
    decrypted = caesar_cipher(encrypted, key, mode='decrypt')

    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
