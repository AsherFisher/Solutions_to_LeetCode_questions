# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverseVowels(s):
    lenS = len(s) - 1
    t = list(s)
    half = int(lenS / 2) + 1 if lenS/2 != 0 else int(lenS / 2)
    j = lenS

    vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

    for i in range(half):
        if not s[i] in vowels:
            continue
        while s[j] not in vowels:
            j -= 1
        temp = t[j]
        t[j] = t[i]
        t[i] = temp
        j -= 1

    listToStr = ''.join(map(str, t))
    return listToStr


if __name__ == "__main__":
    print(reverseVowels("No, it never propagates If i set a \"gap\" or prevention."))
