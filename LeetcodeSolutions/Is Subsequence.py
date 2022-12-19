# בהינתן שתי מחרוזות s ו-t, החזר אמת אם s הוא רצף של t, או false אחרת.
#
# רצף משנה של מחרוזת היא מחרוזת חדשה שנוצרת מהמחרוזת המקורית על ידי מחיקת חלק (לא יכול להיות אף אחד) מהתווים
# מבלי להפריע למיקומם היחסי של התווים הנותרים. (כלומר, "ace" הוא רצף של "abcde" בעוד "aec" אינו).


def isSubsequence(s, t):

    temp = 0
    sizeS = len(s)

    if sizeS == 0:
        return True

    for i in t:
        if i == s[temp]:
            temp += 1
        if temp == sizeS:
            return True
    return False


if __name__ == "__main__":
    print(isSubsequence("b", "c"))
