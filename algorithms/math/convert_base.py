def convert_base(val: str, base: int):
    if base < 0 or (base > 10 and base !=16):
        return -1
    value = 0
    for i, digit in enumerate(val):
        digit_val = convert_digit_to_int(digit)
        if digit_val < 0 or digit_val > base:
            return -1
        # print(digit_val, base ** (len(val)-i-1))
        value += digit_val * (base ** (len(val)-i-1))
    return value


def convert_digit_to_int(char: str):
    if len(char) != 1 or ord(char) > ord('f'):
        return -1
    return int(char,16)
