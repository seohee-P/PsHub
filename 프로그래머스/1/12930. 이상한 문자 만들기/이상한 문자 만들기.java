class Solution {
    public String solution(String s) {
        int count = 0;
        StringBuilder sb = new StringBuilder("");
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == ' '){
                sb.append(" ");
                count = 0;
                continue;
            }
            if(count % 2 == 0)
                sb.append(Character.toString(s.charAt(i)).toUpperCase());
            else
                sb.append(Character.toString(s.charAt(i)).toLowerCase());
            count += 1;
        }
        return sb.toString();
            
    }
}