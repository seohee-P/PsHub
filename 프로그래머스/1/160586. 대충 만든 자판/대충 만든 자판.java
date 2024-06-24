class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        for (int i = 0; i < targets.length; i++){
            for (int j = 0; j < targets[i].length(); j++){
                int push = 101;
                for (String s: keymap){
                    int idx = s.indexOf(targets[i].charAt(j));
                    //System.out.println(idx);
                    if (idx >= 0)
                        push = Math.min(push, idx);
                    //System.out.print(targets[i].charAt(j));
                    //System.out.println(push);
                }
                if (push == 101) {
                    answer[i] = -1;
                    break;
                }
                answer[i] += push+1;
            }
        }
        return answer;
    }
}