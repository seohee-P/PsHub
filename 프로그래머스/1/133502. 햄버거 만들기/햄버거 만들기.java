import java.util.*;
class Solution {
    public static int solution(int[] ingredient) {
        int answer = 0;
        int[] step = {3,2,1};
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < ingredient.length; i++) {
            if (stack.size() >= 3 && ingredient[i] == 1){
                boolean hamburger = true;
                Iterator<Integer> reverseIterator = stack.descendingIterator();
                for(int j = 0; j < 3; j++){
                    if (reverseIterator.next() != step[j]){
                        hamburger = false;
                        break;
                    }
                }
                if (hamburger) {
                    for (int j = 0; j < 3; j++)
                        stack.pollLast();
                    answer += 1;
                    continue;
                }
            }
            stack.add(ingredient[i]);

        }
        return answer;
    }
}