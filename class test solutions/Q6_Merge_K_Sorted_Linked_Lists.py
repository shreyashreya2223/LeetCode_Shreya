# Q6. Merge K Sorted Linked Lists
# Time: O(N log k) | Space: O(k)
#
# Uses the standard LeetCode ListNode definition.

import heapq

def mergeKLists(lists):
    min_heap = []

    for list_index, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, list_index, node))

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        value, list_index, node = heapq.heappop(min_heap)

        current.next = node
        current = node

        if node.next:
            heapq.heappush(
                min_heap,
                (node.next.val, list_index, node.next)
            )

    return dummy.next
