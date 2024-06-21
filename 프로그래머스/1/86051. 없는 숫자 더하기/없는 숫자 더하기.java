class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int[] count = new int[10];
        for (int i = 0; i < 10; i++)
            count[i] = 0;
        for (int i = 0; i< numbers.length; i++)
            count[numbers[i]] += 1;
        for (int i = 0; i < 10; i++)
            if (count[i] == 0)
                answer += i;
        return answer;
    }
}