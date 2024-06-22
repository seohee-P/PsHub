class Solution {
    public long solution(long n) {
        long answer = 0;
        long sqr = (long)Math.sqrt(n);
        if (sqr*sqr == n)
            return (sqr+1)*(sqr+1);
        return -1;
    }
}