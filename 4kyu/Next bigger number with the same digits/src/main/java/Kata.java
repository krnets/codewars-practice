import java.util.Arrays;

public class Kata {
    public static long nextBiggerNumber(long n) {
        char[] digits = String.valueOf(n).toCharArray();

        return findNext(digits, digits.length);
    }

    private static long findNext(char[] digits, int length) {
        int i;
        for (i = length - 1; i > 0; i--) {
            if (digits[i] > digits[i - 1])
                break;
        }
        if (i == 0) {
            return -1L;
        }
        int min = i;
        int last = digits[i - 1];
        for (int j = i + 1; j < length; j++) {
            if (digits[j] > last && digits[j] < digits[min])
                min = j;
        }
        swap(digits, i - 1, min);
        Arrays.sort(digits, i, length);

        return Long.parseLong(new String(digits));
    }

    private static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
