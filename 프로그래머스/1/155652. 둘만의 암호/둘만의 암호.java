class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            int jump = 0, cur = (int)s.charAt(i);
            while(jump != index){
                jump++;
                cur++;
                if (cur > 122)
                    cur -= 26;
                if (skip.contains(Character.toString((char)cur)))
                    jump--;
            }
            sb.append((char)cur);
        }
        return sb.toString();
    }
}