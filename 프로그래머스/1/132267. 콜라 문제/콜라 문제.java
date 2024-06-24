class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n >= 2){
            int get = n/a*b;
            if (get == 0) break;
            answer += get;
            n = get + n%a;
            
        }
        return answer;
    }
}