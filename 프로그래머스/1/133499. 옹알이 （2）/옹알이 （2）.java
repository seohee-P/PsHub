class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        for (int i = 0; i < babbling.length; i++){
            String temp = babbling[i].replace("aya", "1").replace("ye", "2").replace("woo", "3").replace("ma", "4");
            
            boolean speak = true;
            for (int j = 0; j < temp.length(); j++) {
                if ((int)temp.charAt(j) >= 58) {
                    speak = false;
                    break;
                }
                if (j >= 1 && temp.charAt(j) == temp.charAt(j-1)){
                    speak = false;
                    break;
                }
            }
            if(speak) answer++;
        }
        return answer;
    }
}