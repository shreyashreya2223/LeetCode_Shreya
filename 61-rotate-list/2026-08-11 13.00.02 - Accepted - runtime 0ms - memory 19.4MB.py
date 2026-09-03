class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail
        for _ in range(n - k):
            tail = tail.next

        head = tail.next
        tail.next = None

        return head