class Solution:
    def uniqueOccurrences(self, arr):
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        occurrences = list(count.values())

        return len(occurrences) == len(set(occurrences))