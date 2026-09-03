class Solution {
    public int majorityElement(int[] nums) {
        
        int majorityCount = 0;   
        int currentCount = 0;    
        
        for (int num : nums) {
            
            if (currentCount == 0) {
                majorityCount = num;
            }
            
            if (num == majorityCount) {
                currentCount++;
            } else {
                currentCount--;
            }
        }
        
        return majorityCount;
    }
}
