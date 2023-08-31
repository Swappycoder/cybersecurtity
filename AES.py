def rotate_nibble(x):
    return x[4:] + x[:4]


def substitute_nibble(k):
    s_box = [
        ["9", "4", "A", "B"],
        ["D", "1", "8", "5"],
        ["6", "2", "0", "3"],
        ["C", "E", "F", "7"]
    ]

    x1 = int(k[:2], 2)
    y1 = int(k[2:4], 2)
    x2 = int(k[4:6], 2)
    y2 = int(k[6:], 2)

    left, right = s_box[x1][y1], s_box[x2][y2]
    left, right = int(left, 16), int(right, 16)
    return bin(left).replace("0b", "").zfill(4) + bin(right).replace("0b", "").zfill(4)


def xor(a, b):
    return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def generate_keys(key):
    key_in_binary = bin(int(key, 16)).replace("0b", "").zfill(16)

    w = []
    rcon = ["10000000", "00110000"]

    w.append(key_in_binary[:8])
    w.append(key_in_binary[8:])

    yield w[0] + w[1]

    for i in range(2):
        sub_op = substitute_nibble(rotate_nibble(w[-1]))
        left = xor(sub_op, xor(w[-2], rcon[i]))
        right = xor(left, w[-1])

        w.extend([left, right])

        yield left + right


key = "4AF5"
plain_text = "3E6C"

for i, keyI in enumerate(generate_keys(key)):
    print(f"Key {i}: {keyI}")