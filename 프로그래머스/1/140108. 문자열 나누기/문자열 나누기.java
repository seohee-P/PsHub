class Solution {
    public int solution(String s) {
        int answer = 0;
        int idx = 0;
        int a = 0, b = 0;
        while(idx < s.length()){
            char first = s.charAt(idx);
            a = 0; b = 0;
            a++;
            while (a != b && idx < s.length()-1){
                idx++;
                if (s.charAt(idx) != first)
                    b++;
                else
                    a++;
            }
            answer++;
            idx++;
        }
        
        return answer;
    }
}