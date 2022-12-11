# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.

class Solution(object):
    def summaryRanges(self, nums):

        if len(nums) == 0:
            return nums
        retStr = []
        startNum = 0
        lenNums = len(nums)
        add = 0
        i = 0
        while i < lenNums - 1:
            if nums[i] + 1 == nums[i + 1]:
                add += 1
                i += 1
                continue
            if add > 0:
                retStr.append(str(nums[startNum]) + "->" + str(nums[i]))
                i += 1
                add = 0
                startNum = i
            else:
                retStr.append(str(nums[i]))
                startNum = i + 1
                i += 1

        if add > 0:
            retStr.append(str(nums[startNum]) + "->" + str(nums[i]))
        else:
            retStr.append(str(nums[i]))

        return retStr


if __name__ == "__main__":
    a = Solution
    # arr = [0,2,3,4,6,8,9]
    arr = [0,1,2,4,5,7]
    print(a.summaryRanges(a, arr))
