class Solution {
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();
        for (int i = food.length-1; i > 0; i--){
            int div = food[i]/2;
            String f = Integer.toString(i);
            for (int j = 0; j < div; j++){
                sb.insert(0,f);
                sb.append(f);
            }
        }
        sb.insert(sb.length()/2, "0");
        return sb.toString();
    }
}