class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        int n = s.length();

        // Store positions of all 1s
        int[] pos = new int[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                pos[count++] = i;
            }
        }

        // Not enough 1s
        if (count < k) {
            return "";
        }

        String ans = "";
        int minLen = Integer.MAX_VALUE;

        // Check every group of k consecutive 1s
        for (int i = 0; i + k - 1 < count; i++) {
            int start = pos[i];
            int end = pos[i + k - 1];

            int len = end - start + 1;

            String curr = s.substring(start, end + 1);

            if (len < minLen) {
                minLen = len;
                ans = curr;
            } else if (len == minLen && curr.compareTo(ans) < 0) {
                ans = curr;
            }
        }

        return ans;
    }
}