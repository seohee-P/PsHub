import java.util.*;

class Solution {
    public long solution(long n) {
        String s = Long.toString(n);
        String[] arr = new String[s.length()];
        for (int i = 0; i < s.length(); i++){
            arr[i] = Character.toString(s.charAt(i));
        }
        Arrays.sort(arr, Collections.reverseOrder());
        String joinString = String.join("", arr);
        long answer = Long.parseLong(joinString);
        return answer;
    }
}