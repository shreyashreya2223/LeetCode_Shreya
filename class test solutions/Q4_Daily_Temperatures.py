# Q4. Daily Temperatures
# Time: O(n) | Space: O(n)

def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # indices of days waiting for a warmer temperature

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            previous = stack.pop()
            answer[previous] = i - previous

        stack.append(i)

    return answer


# Example:
# print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
