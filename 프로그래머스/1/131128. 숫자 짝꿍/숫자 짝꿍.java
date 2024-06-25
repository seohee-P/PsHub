class Solution {
    public String solution(String X, String Y) {
        int[] x = new int[10];
        int[] y = new int[10];
        for (int i = 0; i < X.length(); i++){
            int n = Character.getNumericValue(X.charAt(i));
            x[n]++;
        }
        for (int i = 0; i < Y.length(); i++){
            int n = Character.getNumericValue(Y.charAt(i));
            y[n]++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 9; i > -1; i--){
            int count = Math.min(x[i],y[i]);
            String num = Integer.toString(i);
            if (num.equals("0") && count >= 1 && sb.length() == 0)
                sb.append(num);
            else{
                for (int j = 0; j < count; j++)
                    sb.append(num);
            }
        }
        String answer = sb.toString();
        if (answer.equals(""))
            return "-1";
        return sb.toString();
    }
}