class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        int[] storeIndex = new int[26];
        for (int i = 0; i < 26; i++) storeIndex[i] = -1;
        for (int i = 0; i < s.length(); i++){
            int lastIndex = storeIndex[(int)s.charAt(i)-97];
            if (lastIndex == -1)
                answer[i] = -1;
            else
                answer[i] = i-lastIndex;
            storeIndex[(int)s.charAt(i)-97] = i;

        }
        return answer;
    }
}