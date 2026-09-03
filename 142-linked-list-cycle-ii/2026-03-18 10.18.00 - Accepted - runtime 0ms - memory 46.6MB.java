public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        ListNode slow = head;
        ListNode fast = head;
        
        // Step 1: Detect cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) {
                
                // Step 2: Find cycle start
                ListNode start = head;
                
                while (start != slow) {
                    start = start.next;
                    slow = slow.next;
                }
                
                return start;
            }
        }
        
        return null;
    }
}