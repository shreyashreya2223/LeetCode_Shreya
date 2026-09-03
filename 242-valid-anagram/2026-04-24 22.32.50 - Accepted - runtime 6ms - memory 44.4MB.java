class Solution {
    public boolean isAnagram(String s, String t) {
        
        // If lengths are different, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        int[] count = new int[26]; // for lowercase English letters

        // Count characters of s and subtract characters of t
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        // Check if all counts are zero
        for (int num : count) {
            if (num != 0) {
                return false;
            }
        }

        return true;
    }
}