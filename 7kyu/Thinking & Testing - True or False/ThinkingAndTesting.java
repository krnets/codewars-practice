/*
public class ThinkingAndTesting {
    public static int testTrueFalse(int n) {
        return Integer.toBinaryString(n).replace("0", "").length();
    }
}*/

public class ThinkingAndTesting {
    public static int testTrueFalse(int n) {
        return Integer.bitCount(n);
    }
}

/*
public class ThinkingAndTesting {
    public static int testTrueFalse(int n) {
        int count = 0;
        while (n > 0) {
            count += 1;
            n = n & (n - 1);
        }
        return count;
    }
}*/
