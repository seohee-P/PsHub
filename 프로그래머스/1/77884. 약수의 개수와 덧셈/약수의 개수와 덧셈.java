class Solution {
    public int solution(int left, int right) {
        // 약수의 개수가 홀수일려면 완전제곱수.
        int answer = 0;
        for(int i = left; i < right + 1; i++){
            int sqr = (int)Math.sqrt(i);
            if (sqr*sqr == i)
                answer -= i;
            else
                answer += i;
        }
        return answer;
    }
}