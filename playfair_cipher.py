def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()

    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix.append(char)

    for ascii_val in range(ord('A'), ord('Z') + 1):
        char = chr(ascii_val)
        if char == 'J':
            continue
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None


def prepare_text(text):
    text = "".join(c.upper() for c in text if c.isalpha()).replace("J", "I")
    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'

    return prepared


def process_digraph(matrix, a, b, mode='encrypt'):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    shift = 1 if mode == 'encrypt' else -1

    if row_a == row_b:
        return (matrix[row_a][(col_a + shift) % 5] +
                matrix[row_b][(col_b + shift) % 5])

    elif col_a == col_b:
        return (matrix[(row_a + shift) % 5][col_a] +
                matrix[(row_b + shift) % 5][col_b])

    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def cipher_codec(text, key, mode='encrypt'):
    matrix = generate_matrix(key)

    if mode == 'encrypt':
        processed_text = prepare_text(text)
    else:
        processed_text = "".join(c.upper() for c in text if c.isalpha())

    result = ""

    for i in range(0, len(processed_text), 2):
        result += process_digraph(
            matrix,
            processed_text[i],
            processed_text[i + 1],
            mode
        )

    return result


if __name__ == "__main__":
    keyword = "MONARCHY"
    plaintext = "instruments"

    print(f"Keyword: {keyword}")
    print(f"Plaintext: {plaintext}")

    encrypted = cipher_codec(plaintext, keyword, mode='encrypt')
    print(f"Ciphertext: {encrypted}")

    decrypted = cipher_codec(encrypted, keyword, mode='decrypt')
    print(f"Decrypted: {decrypted}")
