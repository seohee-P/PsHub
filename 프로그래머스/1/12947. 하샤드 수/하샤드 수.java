class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        int sum = 0;
        String s = Integer.toString(x);
        for (int i = 0; i < s.length(); i++)
            sum += Character.getNumericValue(s.charAt(i));
        if (x % sum == 0)
            answer = true;
        return answer;
    }
}