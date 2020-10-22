/*
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

        N! = 1 * 2 * 3 * ... * N

        Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples

        zeros(6) = 1
        # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

        zeros(12) = 2
        # 12! = 479001600 --> 2 trailing zeros

Hint: You're not meant to calculate the factorial.
Find another way to find the number of zeros.
*/


/*
public class Solution {
    public static int zeros(int n) {
        int count = 0;
        int divideByFive = n;

        for (int i = 5; divideByFive > 0; i *= 5) {
            divideByFive = n / i;
            count += divideByFive;
        }
        return count;
    }
}*/

/*
public class Solution {
    public static int zeros(int n) {
        int count = 0;

        for (int i = 5; i < n; i *= 5) {
            count += n / i;
        }
        return count;
    }
}
*/

/*
public class Solution {
    public static int zeros(int n) {
        if (n == 0) return 0;
        return n / 5 + zeros(n / 5);
    }
}
*/

/*
public class Solution {
    public static int zeros(int n) {
        return n < 5 ? 0 : n / 5 + zeros(n / 5);
    }
}
*/

/*
public class Solution {
    public static int zeros(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
}
*/

/*
public class Solution {
    public static int zeros(int n) {
        int num = (int) (Math.log(n) / Math.log(5));
        int count = 0;
        for (int i = 0; i < num; i++) {
            count += n / Math.pow(5, num);
        }
        return count;
    }
}
*/

/*
public class Solution {
    public static int zeros(int n) {
        return n / 5 + n / 25 + n / 125 + n / 625 + n / 3125 + n / 15625 + n / 78125 + n / 390625 + n / 1953125 + n / 9765625 + n / 48828125 + n / 244140625;
    }
}
*/

/*
public class Solution {
    public static int zeros(int n) {
        int s = 0;
        int k = 1;

        while (n / k > 0) {
            k *= 5;
            s += n / k;
        }
        return s;
    }
}*/

public class Solution {
    public static int zeros(int n) {
        int count = 0;

        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
}
