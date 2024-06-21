import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            int[] answer = {-1};
            return answer;
        }
        else {
            int min = Arrays.stream(arr).min().orElse(0);
            int[] answer = {};
            List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList());
            list.remove(Integer.valueOf(min));
            answer = list.stream().mapToInt(i -> i).toArray();
            return answer;
        }
    }
}