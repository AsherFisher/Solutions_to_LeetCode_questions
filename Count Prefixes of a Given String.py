# Return the number of strings in words that are a prefix of s.
# A prefix of a string is a substring that occurs at the beginning of the string.
# A substring is a contiguous sequence of characters within a string.

def countPrefixes(words, s):
    if not words or not s:
        return 0

    lenS = len(s)

    ret = 0

    for i in words:
        location = 0
        while location < len(i) and location < lenS:
            if len(i) > lenS:
                break
            if i[location] == s[location]:
                location += 1
            else:
                location = 0
                break

        if location > 0:
            ret += 1

    return ret


if __name__ == "__main__":
    print(countPrefixes(["abcd", "b", "c", "ab", "bc", "abc"], "abc"))
