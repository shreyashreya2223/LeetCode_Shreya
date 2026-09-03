class Solution:
    def compress(self, chars):
        read = 0
        write = 0

        while read < len(chars):
            current = chars[read]
            count = 0

            # Count consecutive characters
            while read < len(chars) and chars[read] == current:
                read += 1
                count += 1

            # Write the character
            chars[write] = current
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write