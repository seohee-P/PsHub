class Solution {
    public static int solution(int n, int m, int[] section) {
        int answer = 0;
        int index = 0;
        for (int i = 0; i < section.length; i++) {
            if (section[i] < index) {
                continue;
            }
            index = section[i]+m;
            answer += 1;
        }
        return answer;
    }
}