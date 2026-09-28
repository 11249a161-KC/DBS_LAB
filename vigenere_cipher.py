def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            char_pos = ord(char) - start
            if mode == 'encrypt':
                new_pos = (char_pos + shift) % 26
            elif mode == 'decrypt':
                new_pos = (char_pos - shift) % 26
            else:
                raise ValueError("Mode must be either 'encrypt' or 'decrypt'")

            result.append(chr(start + new_pos))

            key_index += 1
        else:
            result.append(char)

    return "".join(result)

if __name__ == "__main__":
    secret_key = 'PYTHON'
    original_message = "Hello World! Vigenere cipher in Python."

    ciphertext = vigenere_cipher(original_message, secret_key, mode='encrypt')
    print(f"Original:  {original_message}")
    print(f"Encrypted: {ciphertext}")

    unciphertext = vigenere_cipher(original_message, secret_key, mode='decrypt')
    print(f"Original:  {original_message}")
    print(f"Encrypted: {decrypted_message}")

    
