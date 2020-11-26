public class Solution {
    public static String lcs(String x, String y) {
        var sb = new StringBuilder();
        int pos = 0;

        for (int i = 0; i < y.length(); i++) {
            for (int j = pos; j < x.length(); j++) {
                if (x.charAt(j) == y.charAt(i)) {
                    sb.append(y.charAt(i));
                    pos++;
                    break;
                }
            }
        }
        return sb.toString();
    }
}

