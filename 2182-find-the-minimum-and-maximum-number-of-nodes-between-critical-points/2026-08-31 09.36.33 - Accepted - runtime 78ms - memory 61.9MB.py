class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        
        prev = head
        curr = head.next
        pos = 1
        
        first = -1
        prev_critical = -1
        min_dist = float('inf')
        
        while curr.next:
            next_node = curr.next
            
            # Check if current node is a critical point
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val
            
            if is_max or is_min:
                
                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - prev_critical)
                
                prev_critical = pos
            
            prev = curr
            curr = next_node
            pos += 1
        
        # Fewer than two critical points
        if first == -1 or first == prev_critical:
            return [-1, -1]
        
        max_dist = prev_critical - first
        
        return [min_dist, max_dist]