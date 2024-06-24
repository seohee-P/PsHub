import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        // lottos 0의 개수 세기
        int countZero = 0;
        for (int i = 0; i < lottos.length; i++) {
            if (lottos[i] == 0) countZero++;
        }
        Set<Integer> set1 = new HashSet<>(Arrays.stream(lottos).boxed().collect(Collectors.toList()));
        Set<Integer> set2 = new HashSet<>(Arrays.stream(win_nums).boxed().collect(Collectors.toList()));
        set1.retainAll(set2);
        
        if (set1.size() <= 1) answer[1] = 6;
        else answer[1] = 7 - set1.size();
        if (set1.size()+countZero <= 1) answer[0] = 6;
        else answer[0] = 7 - (set1.size()+countZero);
        
        return answer;
    }
}