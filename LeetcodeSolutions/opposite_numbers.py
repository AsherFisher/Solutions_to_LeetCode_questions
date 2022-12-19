# רשימה ובה מספרים שלמים חיוביים ושלמים, מצא את המספרים שהם נגדיים אחד לשני


def opposite_numbers(array):
    array.sort()

    ret_arr = set()

    for i in array:
        if -i in ret_arr:
            print(i)
        ret_arr.add(i)


if __name__ == "__main__":
    opposite_numbers([1, 2, -3, 3, -7, 5, 4, -1, 4, 5])