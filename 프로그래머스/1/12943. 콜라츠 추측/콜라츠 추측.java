class Solution {
    public int solution(int num) {
        int answer = 0;
        Long n = Long.valueOf(num);
        while(n != 1 && answer <= 500) {
            if (n % 2 == 0)
                n /= 2;
            else
                n = n * 3 + 1;
            answer += 1;
        }
        if (answer > 500)
            return -1;
        else
            return answer;
    }
}