class Solution {
    public int f(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int last = f(n-1);
        int lastsec = f(n-2);
        return last + lastsec;
    }
}