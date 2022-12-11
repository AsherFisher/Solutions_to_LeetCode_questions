# add one number for any input number

def plusOne(digits):
    size = len(digits) - 1

    if digits[size] < 9:
        digits[size] += 1
        return digits

    for i in range(0, size + 1):
        if digits[size - i] < 9:
            digits[size - i] += 1
            return digits
        else:
            digits[size - i] = 0

    digits[0] = 1
    digits.append(0)
    return digits


if __name__ == "__main__":
    i = [9]
    print(plusOne(i))