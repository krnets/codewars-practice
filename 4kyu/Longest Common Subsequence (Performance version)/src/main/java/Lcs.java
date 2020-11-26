public class Lcs {

    static String lcs(String a, String b) {
        int[][] grid = new int[a.length() + 1][b.length() + 1];
        var sb = new StringBuilder();

        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                if (a.charAt(i) == b.charAt(j))
                    grid[i + 1][j + 1] = 1 + grid[i][j];
                else
                    grid[i + 1][j + 1] = Math.max(grid[i + 1][j], grid[i][j + 1]);
            }
        }

        for (int i = a.length(), j = b.length(); i > 0 && j > 0; ) {
            if (grid[i][j] == grid[i - 1][j])
                i--;
            else if (grid[i][j] == grid[i][j - 1])
                j--;
            else if (a.charAt(i - 1) == b.charAt(j - 1)) {
                sb.append(a.charAt(i - 1));
                i--;
                j--;
            }
        }
        return sb.reverse().toString();
    }
}