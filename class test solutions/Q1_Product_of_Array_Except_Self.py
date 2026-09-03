# Q1. Product of Array Except Self
# Time: O(n) | Extra space: O(1), excluding output

def productExceptSelf(nums):
    answer = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# Example:
# print(productExceptSelf([1, 2, 3, 4]))
# Output: [24, 12, 8, 6]
