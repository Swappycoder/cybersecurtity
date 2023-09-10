def hex_to_bin(k, size=16):
    return bin(int(k, 16)).replace("0b", "").zfill(size)


def bin_to_hex(k, size=4):
    return hex(int(k, 2)).replace("0x", "").zfill(size)


def xor(a, b):
    return "".join([hex(int(a[i], 16) ^ int(b[i], 16))[2:] for i in range(len(a))])


def str_to_matrix(s):
    return [
        [int(s[:4], 2), int(s[8:12], 2)],
        [int(s[4:8], 2), int(s[12:], 2)]
    ]


def matrix_to_str(m):
    return hex_to_bin(m[0][0], 4) + hex_to_bin(m[1][0], 4) + hex_to_bin(m[0][1], 4) + hex_to_bin(m[1][1], 4)


def rotate_nibble(x):
    return x[4:] + x[:4]


def substitute_nibble(k):
    s_box = [
        ["9", "4", "A", "B"],
        ["D", "1", "8", "5"],
        ["6", "2", "0", "3"],
        ["C", "E", "F", "7"]
    ]

    n = len(k) // 4

    res = ""

    for i in range(n):
        x = int(k[4 * i: 4 * i + 2], 2)
        y = int(k[4 * i + 2: 4 * i + 4], 2)

        res += hex_to_bin(s_box[x][y], 4)

    return res


def generate_keys(key):
    key_in_binary = hex_to_bin(key)

    w = []
    rcon = ["10000000", "00110000"]

    w.append(key_in_binary[:8])
    w.append(key_in_binary[8:])

    yield bin_to_hex(w[0] + w[1])

    for i in range(2):
        sub_op = substitute_nibble(rotate_nibble(w[-1]))
        left = xor(sub_op, xor(w[-2], rcon[i]))
        right = xor(left, w[-1])

        w.extend([left, right])

        yield bin_to_hex(left + right)


def shift_rows(matrix):
    return matrix[:4] + matrix[12:] + matrix[8:12] + matrix[4:8]


def mix_columns(s):
    lookup = {
        1: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"],
        2: ["0", "2", "4", "6", "8", "A", "C", "E", "3", "1", "7", "5", "B", "9", "F", "D"],
        4: ["0", "4", "8", "C", "3", "7", "B", "F", "6", "2", "E", "A", "5", "1", "D", "9"],
        9: ["0", "9", "1", "8", "2", "B", "3", "A", "4", "D", "5", "C", "6", "F", "7", "E"],
    }

    s = str_to_matrix(s)
    M = [[1, 4], [4, 1]]
    _s = [[0, 0], [0, 0]]

    def mmul(i, j): return lookup[i][j]

    _s[0][0] = xor(mmul(M[0][0], s[0][0]), mmul(M[0][1], s[1][0]))
    _s[0][1] = xor(mmul(M[0][0], s[0][1]), mmul(M[0][1], s[1][1]))
    _s[1][0] = xor(mmul(M[1][0], s[0][0]), mmul(M[1][1], s[1][0]))
    _s[1][1] = xor(mmul(M[1][0], s[0][1]), mmul(M[1][1], s[1][1]))
    return matrix_to_str(_s)


def roundI(ci, k, round):
    if round == 0:
        return xor(ci, k)
    subNib = substitute_nibble(hex_to_bin(ci))
    shRow = shift_rows(subNib)
    mixCol = shRow
    if round != 2:
        mixCol = mix_columns(shRow)

    return xor(bin_to_hex(mixCol), k)


key = "4AF5"
plain_text = input("Enter 16-bit plain text in hexadecimal: ").upper()
current_iteration = plain_text

# 1101 0111 0010 1000
for i, keyI in enumerate(generate_keys(key)):
    current_iteration = roundI(current_iteration, keyI, i)

cipher_text = current_iteration.upper()

print("Cipher text: ", cipher_text)
