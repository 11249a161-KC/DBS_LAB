import math

def rail_fence_encrypt(text, rails):
    if rails == 1:
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return "".join(["".join(row) for row in fence])


def rail_fence_decrypt(cipher, rails):
    if rails == 1:
        return cipher

    matrix = [["\n" for _ in range(len(cipher))] for _ in range(rails)]

    rail = 0
    direction = 1

    for i in range(len(cipher)):
        matrix[rail][i] = "*"
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if matrix[r][c] == "*" and index < len(cipher):
                matrix[r][c] = cipher[index]
                index += 1

    result = []
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        result.append(matrix[rail][i])
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return "".join(result)


def get_col_order(key):
    return sorted(range(len(key)), key=lambda k: key[k])


def columnar_encrypt(text, key, padding_char="_"):
    key_len = len(key)

    extra_chars = len(text) % key_len
    if extra_chars != 0:
        text += padding_char * (key_len - extra_chars)

    rows = [text[i:i + key_len] for i in range(0, len(text), key_len)]

    col_order = get_col_order(key)
    cipher = ""

    for col_idx in col_order:
        cipher += "".join([row[col_idx] for row in rows])

    return cipher


def columnar_decrypt(cipher, key):
    key_len = len(key)
    num_rows = math.ceil(len(cipher) / key_len)

    matrix = [["" for _ in range(key_len)] for _ in range(num_rows)]
    col_order = get_col_order(key)

    index = 0

    for col_idx in col_order:
        for row_idx in range(num_rows):
            if index < len(cipher):
                matrix[row_idx][col_idx] = cipher[index]
                index += 1

    plaintext = ""

    for row in matrix:
        plaintext += "".join(row)

    return plaintext


if __name__ == "__main__":
    message = "GeeksforGeeks"

    rf_key = 3
    rf_encrypted = rail_fence_encrypt(message, rf_key)
    rf_decrypted = rail_fence_decrypt(rf_encrypted, rf_key)

    print(f"Original Text : {message}")
    print(f"Rails         : {rf_key}")
    print(f"Encrypted Text: {rf_encrypted}")
    print(f"Decrypted Text: {rf_decrypted}\n")

    col_key = "HACK"
    col_encrypted = columnar_encrypt(message, col_key)
    col_decrypted = columnar_decrypt(col_encrypted, col_key)

    print(f"Original Text : {message}")
    print(f"Key           : {col_key}")
    print(f"Encrypted Text: {col_encrypted}")
    print(f"Decrypted Text: {col_decrypted}")
