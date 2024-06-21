import java.util.*;

class Solution {
    public int[] solution(long n) {
        String s = Long.toString(n);
        int[] answer = new int[s.length()];
        for (int i = s.length()-1; i > -1; i--){
            answer[s.length()-1-i] = Character.getNumericValue(s.charAt(i));
        }
        return answer;
    }
}