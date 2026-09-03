class Solution {

    public int climbStairs(int n) {
        return f(0, n); 
    }

    public int f(int i, int n) {

        if (i == n) return 1; 
        if (i > n) return 0; 

        int left = f(i + 1, n);
        int right = f(i + 2, n); 

        return left + right;
    }
}