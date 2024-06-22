import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < i; j++)
                set.add(numbers[j]+numbers[i]);
        }
        List<Integer> res = new ArrayList<>(set);
        int[] answer = res.stream().sorted().mapToInt(i -> i).toArray();

        return answer;
    }
}