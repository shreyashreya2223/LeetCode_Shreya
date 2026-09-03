import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        small = []   # max heap (use negative values)
        large = []   # min heap
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def add(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            balance()

        def remove(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= -small[0]:
                small_size -= 1
            else:
                large_size -= 1

            clean()
            balance()

        def clean():
            while small and delayed[-small[0]] > 0:
                num = -heapq.heappop(small)
                delayed[num] -= 1

            while large and delayed[large[0]] > 0:
                num = heapq.heappop(large)
                delayed[num] -= 1

        def balance():
            nonlocal small_size, large_size

            # small can have at most one more element than large
            if small_size > large_size + 1:
                num = -heapq.heappop(small)
                heapq.heappush(large, num)

                small_size -= 1
                large_size += 1

            elif small_size < large_size:
                num = heapq.heappop(large)
                heapq.heappush(small, -num)

                large_size -= 1
                small_size += 1

            clean()

        # First window
        for i in range(k):
            add(nums[i])

        result = []

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        result.append(get_median())

        # Slide window
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])

            result.append(get_median())

        return result