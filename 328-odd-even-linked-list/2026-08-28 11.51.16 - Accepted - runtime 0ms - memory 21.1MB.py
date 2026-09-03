class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            # Connect current odd node to next odd node
            odd.next = even.next
            odd = odd.next

            # Connect current even node to next even node
            even.next = odd.next
            even = even.next

        # Put even list after odd list
        odd.next = even_head

        return head