class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return find(nums, target, 0, 0);
    }

    int find(int[] nums, int target, int i, int sum) {
        if (i == nums.length) {
            if (sum == target) return 1;
            else return 0;
        }

        int left = find(nums, target, i + 1, sum + (-nums[i]));
        int right = find(nums, target, i + 1, sum + (nums[i]));
        return left + right;
    }
}