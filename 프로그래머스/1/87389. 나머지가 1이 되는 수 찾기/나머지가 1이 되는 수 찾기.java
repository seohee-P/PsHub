import java.util.*;

class Solution {
    public int solution(int n) {
        // 나머지가 1이 되는 수를 제일 작은 수를 찾는 문제.
        int x = 2;
        while (true) {
            if (n % x == 1) {
                break;
            }
            x++;
        }

        return x;
    }
}