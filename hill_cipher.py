import numpy as np

def text_to_vector(text):
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def vector_to_text(vector):
    return "".join(chr(num + ord('A')) for num in vector)

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_element = det % modulus

    det_inverse = -1
    for i in range(1, modulus):
        if (det_element * i) % modulus == 1:
            det_inverse = i
            break

    if det_inverse == -1:
        raise ValueError("The key matrix is not invertible modulo 26. Choose a different key.")

    matrix_inverse = np.linalg.inv(matrix) * det
    adjugate_matrix = np.round(matrix_inverse).astype(int) % modulus

    return (det_inverse * adjugate_matrix) % modulus

def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    numbers = text_to_vector(plaintext)

    while len(numbers) % n != 0:
        numbers.append(23)

    ciphertext_vector = []

    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext_vector.extend(encrypted_block)

    return vector_to_text(ciphertext_vector)

def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    numbers = text_to_vector(ciphertext)
    inv_key_matrix = matrix_mod_inverse(key_matrix, 26)

    plaintext_vector = []

    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        decrypted_block = np.dot(inv_key_matrix, block) % 26
        plaintext_vector.extend(decrypted_block)

    return vector_to_text(plaintext_vector)

if __name__ == "__main__":
    key = np.array([[3, 3],
                    [2, 5]])

    message = "HELLO"
    print(f"Original Message: {message}")

    encrypted_msg = encrypt(message, key)
    print(f"Encrypted Ciphertext: {encrypted_msg}")

    decrypted_msg = decrypt(encrypted_msg, key)
    print(f"Decrypted Plaintext: {decrypted_msg}")
