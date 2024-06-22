class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        boolean isSmall;
        for (int i = 0; i< t.length()-p.length()+1; i++){
            isSmall = true;
            for (int j = 0; j < p.length(); j++){
                if (t.charAt(i+j) > p.charAt(j)){
                    isSmall = false;
                    break;
                }
                else if (t.charAt(i+j) < p.charAt(j)){
                    break;
                }
            }
            if (isSmall)
                answer += 1;
        }
        return answer;
    }
}