class Solution:
    def pairSum(self, head):
        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare first half with reversed second half
        left = head
        right = prev
        max_sum = 0

        while right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next

        return max_sum