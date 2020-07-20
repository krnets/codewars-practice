/*
Let us begin with an example:

        Take a number: 56789. Rotate left, you get 67895.
        Keep the first digit in place and rotate left the other digits: 68957.
        Keep the first two digits in place and rotate the other ones: 68579.
        Keep the first three digits and rotate left the rest: 68597.
        Now it is over since keeping the first four it remains only one digit which rotated is itself.

        You have the following sequence of numbers:

        56789 -> 67895 -> 68957 -> 68579 -> 68597

        return the greatest: 68957.

        Write function max_rot(n) which given a positive integer n returns the maximum number
        rotations similar to the above example.

        So maxRot is such as:

        max_rot(56789) should return 68957
        max_rot(38458215) should return 85821534
*/

/*
public class MaxRotate {
    public static long maxRot(long n) {
        long max = n;
        long digit = 1;
        while (n / 10 >= digit) {
            digit *= 10;
        }
        long fixed = 0;
        long remainder = n;
        while (digit > 1) {
            long rotated = (remainder % digit) * 10 + remainder / digit;
            fixed += rotated / digit * digit;
            remainder = rotated % digit;
            max = Math.max(max, fixed + remainder);
            digit /= 10;
        }
        return max;
    }
}*/

public class MaxRotate {
    public static long maxRot(long n) {
        String num = String.valueOf(n);
        for (int i = 0; i < num.length() - 1; i++) {
            num = num.substring(0, i) + num.substring(i + 1) + num.charAt(i);
            long current = Long.parseLong(num);
            if (current > n)
                n = current;
        }
        return n;
    }
}
