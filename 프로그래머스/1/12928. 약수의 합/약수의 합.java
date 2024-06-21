import java.util.*;
class Solution {
    public int solution(int n) {
        // 모든 약수를 더하는 문제.
        int answer = 0;
        for (int i = 1; i <= n; i++){
            if (n % i==0) {
                answer += i;
            }
        }

        return answer;
    }
}