import java.util.*;

class Solution {
   public int[] solution(int[] arr, int divisor) {

        //리스트 만들기
        List<Integer> list = new ArrayList<>();

        //  반복문으로 arr 배열만큼 돌기
        for(int i=0; i<arr.length; i++) {
            // divisor로 나누어 떨어졌을때 0이면 리스트 넣기
            if(arr[i]%divisor == 0) {
                list.add(arr[i]);
            } 
        } 
        if(list.size() == 0) {
            list.add(-1);
        }
        //리스트 정렬하기
        Collections.sort(list);
        //리스트를 int 배열로 만들기(방법 1: 반복문/ 방법 2:stream 사용)
        int[] answer = new int[list.size()];
        for(int i=0; i<=list.size()-1; i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}