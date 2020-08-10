public class ThinkingAndTesting {
    public static int testTrueFalse(int n) {
        return Integer.toBinaryString(n).replace("0", "").length();
    }
}