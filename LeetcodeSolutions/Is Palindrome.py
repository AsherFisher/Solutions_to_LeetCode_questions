# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
import re


def isPalindrome(s):
    clean_phrase = re.sub('[^a-zA-Z0-9]', '', s.lower())

    return clean_phrase == clean_phrase[::-1]


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
