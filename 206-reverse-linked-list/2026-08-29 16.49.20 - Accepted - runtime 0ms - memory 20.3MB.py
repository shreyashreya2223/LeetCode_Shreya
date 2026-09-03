class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next node
            curr.next = prev        # reverse the pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev