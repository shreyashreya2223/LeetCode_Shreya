class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs.values():  # Opening bracket
                stack.append(ch)
            else:  # Closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack