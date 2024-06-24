import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        //System.out.println(Arrays.toString(score));
        for (int i = score.length-1; i > -1; i-=m){
            //System.out.println(i-m);
            if(i-m < -1) continue;
            int[] copy = Arrays.copyOfRange(score, i-m+1, i+1);
            //System.out.println(Arrays.toString(copy));
            List<Integer> list = Arrays.stream(copy).boxed().collect(Collectors.toList());
            int min = Collections.min(list);
            answer += min*m;
        }
        return answer;
    }
}