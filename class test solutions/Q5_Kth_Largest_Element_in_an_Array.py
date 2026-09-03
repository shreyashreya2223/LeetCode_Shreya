# Q5. Kth Largest Element in an Array
# Time: O(n log k) | Space: O(k)

import heapq

def findKthLargest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


# Example:
# print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
# Output: 5
