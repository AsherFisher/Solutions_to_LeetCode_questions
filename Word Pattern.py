# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

class Solution(object):
    def wordPattern(self, pattern, s):
        if not pattern or not s:
            return True

        word_list = s.split()

        if len(pattern) != len(word_list):
            return False

        ret = {}

        for i in range(0, len(word_list)):
            if word_list[i] in ret:
                if ret.get(word_list[i]) != pattern[i]:
                    return False
            if pattern[i] in ret.values():
                if ret.get(word_list[i]) != pattern[i]:
                    return False
                else:
                    continue
            else:
                ret[word_list[i]] = pattern[i]

        return True


if __name__ == "__main__":
    a = Solution
    patternSend = "abba"
    fillStr = "dog cat cat fish"
    print(a.wordPattern(a, patternSend, fillStr))