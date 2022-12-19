# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums

    lenNums = len(nums)

    for i in range(lenNums - 1, -1, -1):
        if nums[i] == 0:
            j = i
            while j + 1 < lenNums:
                if nums[j+1] == 0:
                    break
                nums[j] = nums[j + 1]
                nums[j + 1] = 0
                j += 1

    return nums


if __name__ == "__main__":
    print(moveZeroes([0, 1, 0, 3, 12]))
