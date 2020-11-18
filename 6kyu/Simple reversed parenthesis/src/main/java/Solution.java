public class Solution {
    public static int solve(String str) {
        if (str.length() % 2 != 0) return -1;

        while(str.contains("()")) {
            str = str.replace("()", "");
        }
        int count = 0;

        for (int i = 1; i < str.length(); i+= 2) {
            if (str.charAt(i-1) == str.charAt(i)) {
                count++;
            } else {
                count += 2;
            }
        }
        return count;
    }
}