class Solution {
    public long solution(int price, int money, int count) {
        long answer;
        long sum = 0;
        for (int i = 1; i < count+1; i++){
            sum += price*i;
        }
        long m = Long.valueOf(money);
        answer = sum-m;
        if (answer < 0)
            return 0L;
        return answer;
    }
}