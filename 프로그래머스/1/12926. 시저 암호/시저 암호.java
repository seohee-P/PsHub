class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder("");
        for(int i = 0; i < s.length(); i++){
            if (s.charAt(i) == ' '){
                sb.append(" ");
                continue;
            }
            int ascii = (int)s.charAt(i);
            if (65 <= ascii && ascii <= 90) {
                ascii = ((ascii+n) > 90) ? ascii+n-91+65: ascii+n;
            }
            else
                ascii = ((ascii+n) > 122) ? ascii+n-123+97: ascii+n;
                
            sb.append(Character.toString((char)ascii));
            
        }
        return sb.toString();
    }
}