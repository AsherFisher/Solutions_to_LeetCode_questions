# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    retMax = 0
    temp = 0

    if len(nums) == 0:
        return 0

    for i in nums:
        if i == 1:
            temp += 1
            if temp > retMax:
                retMax += 1
        else:
            temp = 0

    return retMax


if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
