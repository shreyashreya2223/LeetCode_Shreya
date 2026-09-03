class Solution:
    def deleteMiddle(self, head):
        # If only one node exists, deleting the middle
        # leaves an empty list.
        if head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        prev.next = slow.next

        return head