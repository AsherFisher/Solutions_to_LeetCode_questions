# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
    result = 0

    plus = max(nums)

    for i in range(32):
        bit_sum = 0

        for num in nums:
            bit = (num + plus >> i) & 1
            bit_sum += bit

        result |= ((bit_sum % 3) << i)

    return result - plus


if __name__ == "__main__":
    print(singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))
