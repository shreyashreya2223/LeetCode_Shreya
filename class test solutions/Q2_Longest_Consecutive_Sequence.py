# Q2. Longest Consecutive Sequence
# Time: O(n) average | Space: O(n)

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence.
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# Example:
# print(longestConsecutive([100, 4, 200, 1, 3, 2]))
# Output: 4
