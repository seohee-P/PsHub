class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxW, maxH;
        if (sizes[0][0] < sizes[0][1]){
            maxW = sizes[0][1];
            maxH = sizes[0][0];
        }
        else {
            maxW = sizes[0][0];
            maxH = sizes[0][1];
        }
        for (int i = 1; i<sizes.length; i++){
            if (sizes[i][0] < sizes[i][1]) {
                maxW = (maxW < sizes[i][1]) ? sizes[i][1] : maxW;
                maxH = (maxH < sizes[i][0]) ? sizes[i][0] : maxH;
            }
            else {
                maxW = (maxW < sizes[i][0]) ? sizes[i][0] : maxW;
                maxH = (maxH < sizes[i][1]) ? sizes[i][1] : maxH;
            }
        }
        answer = maxH * maxW;
        return answer;
    }
}