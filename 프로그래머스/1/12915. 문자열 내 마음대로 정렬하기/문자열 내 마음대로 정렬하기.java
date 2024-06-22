import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = Arrays.stream(strings)
                .sorted() // 오름차순 정렬
                .sorted(Comparator.comparing(s -> s.charAt(n))) // 2번째 문자를 기준으로 비교해서 오름차순 정렬
                .toArray(String[]::new);
        return answer;

    }
}