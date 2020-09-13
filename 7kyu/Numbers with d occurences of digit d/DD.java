/*
In this kata, we want to discover a small property of numbers.
We say that a number is a dd number if it contains d occurences of a digit d, (d is in [1,9]).

Examples

        664444309 is a dd number, as it contains 4 occurences of the number 4
        30313, 122 are dd numbers as they respectively contain 3 occurences of the number 3,
        and (1 occurence of the number 1 AND 2 occurences of the number 2)
        123109, 0, 56542 are not dd numbers

Task
        Your task is to implement a function called isDD that takes a positive number
        and returns a boolean corresponding to whether the number is a dd number or not.
*/

/*
public class DD {
    public static boolean isDD(int n) {
        for (int i = 1; i < 10; i++) {
            String s = String.valueOf(n);
            s = s.replaceAll("[^" + i + "]", "");
            if (s.length() == i)
                return true;
        }
        return false;
    }
}
*/

public class DD {
    private static final int base = 10;

    public static boolean isDD(int n) {
        int[] digitCount = new int[base];

        while (n > 0) {
            digitCount[n % base]++;
            n /= base;
        }
        for (int i = 0; i < base; i++) {
            if (digitCount[i] == i)
                return true;
        }
        return false;
    }
}
