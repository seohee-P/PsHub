class Solution {
    public int solution(int n) {
        // 최대 지수 알아내기
        int maxPower = 0;
        while(Math.pow(3,maxPower) <= n) {
            maxPower++;
        }
        // 3진법으로 바꾸기
        StringBuilder change3 = new StringBuilder("");
        for(int i = maxPower-1; i > -1; i--){
            int div = n/(int)Math.pow(3,i);
            change3.append(Integer.toString(div));
            n -= (int)Math.pow(3,i)*div;
        }
        // 앞뒤반전
        String change10 = change3.reverse().toString();
        // 10진법으로 전환
        int answer = 0;
        for (int i = maxPower-1; i>-1; i--){
            answer += Math.pow(3,i) * Character.getNumericValue(change10.charAt(change10.length()-1-i));
        }
        
        
        return answer;
    }
}