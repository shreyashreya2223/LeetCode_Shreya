class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Store product of all elements to the left
        left_product = 1

        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Multiply by product of all elements to the right
        right_product = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer