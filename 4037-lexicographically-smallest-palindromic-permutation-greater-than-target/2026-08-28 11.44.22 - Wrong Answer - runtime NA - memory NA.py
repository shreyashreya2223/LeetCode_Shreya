class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        odd = [i for i in range(26) if cnt[i] % 2]

        if len(odd) > 1:
            return ""

        # Build the multiset for the left half
        half = [0] * 26
        for i in range(26):
            half[i] = cnt[i] // 2

        # Middle character
        mid = chr(odd[0] + ord('a')) if odd else ""

        # We only need to compare the first half with target's
        # first half. The second half is forced by the first half.
        m = n // 2
        t_half = target[:m]

        def build_pal(left):
            """Construct palindrome from its left half."""
            left_str = ''.join(chr(i + ord('a')) * left[i]
                               for i in range(26))
            if n % 2:
                return left_str + mid + left_str[::-1]
            return left_str + left_str[::-1]

        # First try to construct the smallest half that is
        # lexicographically >= target's first half.
        #
        # We use backtracking only along the positions where
        # we may need to make the first half larger.
        #
        # Since there are only 26 letters, we can greedily try
        # to keep the prefix equal to target and, when necessary,
        # make one position larger and fill the rest minimally.

        result = [-1] * m

        # Try to match target's first half as long as possible.
        for i in range(m):
            c = ord(t_half[i]) - ord('a')

            if half[c] > 0:
                result[i] = c
                half[c] -= 1
            else:
                # We cannot stay equal.
                # Find the smallest character > c.
                bigger = -1
                for x in range(c + 1, 26):
                    if half[x] > 0:
                        bigger = x
                        break

                if bigger != -1:
                    result[i] = bigger
                    half[bigger] -= 1

                    # Fill remaining positions as small as possible
                    pos = i + 1
                    for x in range(26):
                        while half[x] > 0:
                            result[pos] = x
                            pos += 1
                            half[x] -= 1

                    left = result
                    return build_pal_from_array(left, mid, n)

                # No bigger character here.
                # We need to backtrack and increase an earlier position.
                break

        else:
            # Entire first half matched target.
            # The resulting palindrome may still be <= target,
            # because the second half is forced.
            candidate = build_pal_from_array(result, mid, n)

            if candidate > target:
                return candidate

            # Need the next larger first half.
            # Backtrack below.
            
        # Reconstruct counts from the original string
        half = [c // 2 for c in cnt]

        # Find the rightmost position where we can make the
        # first half larger than target's corresponding character.
        for i in range(m - 1, -1, -1):
            # Count characters used before i according to target
            used = [0] * 26
            possible = True

            for j in range(i):
                c = ord(t_half[j]) - ord('a')
                if half[c] == 0:
                    possible = False
                    break
                used[c] += 1

            if not possible:
                continue

            remaining = half[:]
            for x in range(26):
                remaining[x] -= used[x]

            c = ord(t_half[i]) - ord('a')

            # Pick smallest character strictly larger than target[i]
            bigger = -1
            for x in range(c + 1, 26):
                if remaining[x] > 0:
                    bigger = x
                    break

            if bigger == -1:
                continue

            result = []

            # Prefix equal to target
            for j in range(i):
                result.append(ord(t_half[j]) - ord('a'))

            # Make this position larger
            result.append(bigger)
            remaining[bigger] -= 1

            # Fill suffix minimally
            for x in range(26):
                while remaining[x] > 0:
                    result.append(x)
                    remaining[x] -= 1

            return build_pal_from_array(result, mid, n)

        return ""


def build_pal_from_array(left, mid, n):
    left_str = ''.join(chr(x + ord('a')) for x in left)

    if n % 2:
        return left_str + mid + left_str[::-1]

    return left_str + left_str[::-1]