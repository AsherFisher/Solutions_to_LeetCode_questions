# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s):
    splitS = s.split()
    return (len(splitS[-1]))


if __name__ == "__main__":
    print(lengthOfLastWord("luffy is still joyboy"))
