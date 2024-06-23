import java.util.*;
class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for(int i = 1; i <= number; i++){
            Set<Integer> set = new HashSet<>();
            for(int j = 1; j < (int)Math.sqrt(i)+1; j++){
                if(i%j == 0){
                    set.add(j);
                    set.add(i/j);
                }
            }
            if (set.size() > limit)
                answer += power;
            else answer += set.size();
        }
        return answer;
    }
}