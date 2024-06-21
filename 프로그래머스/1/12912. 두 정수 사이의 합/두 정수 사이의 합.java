class Solution {
    public long solution(int a, int b) {
        if (b < a) {
            int temp = a;
            a = b;
            b = temp;
        }
        long answer = 0;
        for (int i = a; i < b+1; i++) {
            answer += i;
        }
        return answer;
    }
}