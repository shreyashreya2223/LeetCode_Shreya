class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        required = len(need)

        min_length = float("inf")
        result = ""

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            # We just satisfied a required character
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Window is valid
            while have == required:

                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result