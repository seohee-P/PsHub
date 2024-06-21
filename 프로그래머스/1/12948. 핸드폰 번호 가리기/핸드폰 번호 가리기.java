class Solution {
    public String solution(String phone_number) {
        String answer = "";
        for (int i = 0; i < phone_number.length(); i++){
            if (phone_number.length()-1-i <= 3)
                answer += Character.toString(phone_number.charAt(i));
            else
                answer += "*";
                
        }
        return answer;
    }
}