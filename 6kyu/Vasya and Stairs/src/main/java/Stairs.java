public class Stairs {
    public static int NumberOfSteps(int n, int m) {
//        return n < m ? -1 : ((n + 1) / 2 + m - 1) / m * m;
        return n++ < m ? -1 : (n / 2 - 1 + m) / m * m;
    }
}