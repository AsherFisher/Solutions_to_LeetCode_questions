# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s):
    lenS = len(s) - 1
    i = 0

    while i < lenS:
        temp = s[lenS]
        s[lenS] = s[i]
        s[i] = temp
        i += 1
        lenS -= 1

    return s


if __name__ == "__main__":
    print(reverseString(["h", "e", "l", "l", "o"]))
