import java.util.*;

class Solution {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        helper(0, nums, new ArrayList<>(), result);
        return result;
    }
    public void helper(int i, int[] nums, List<Integer> temp, List<List<Integer>> result) {
        if (i == nums.length) {
            result.add(new ArrayList<>(temp));
            return;
        }
        temp.add(nums[i]);
        helper(i + 1, nums, temp, result);
        temp.remove(temp.size() - 1);
        helper(i + 1, nums, temp, result);
    }
}