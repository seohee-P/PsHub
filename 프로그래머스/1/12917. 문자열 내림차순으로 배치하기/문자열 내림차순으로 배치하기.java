import java.util.*;

class Solution {
    public String solution(String s) {
        String[] arr = s.split("");
        
        Arrays.sort(arr, Collections.reverseOrder());
        
        String answer = String.join("", arr);
        return answer;
    }
}