class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < i; j++){
                for (int k = 0; k < j; k++){
                    int sum = nums[i] + nums[j] + nums[k];
                    boolean isPrime = true;
                    for (int s = 2; s < Math.sqrt(sum)+1; s++){
                        if (sum%s == 0){
                            isPrime = false;
                            break;
                        }
                    }
                    if (isPrime) answer += 1;
                }
            }
        }
        return answer;
    }
}