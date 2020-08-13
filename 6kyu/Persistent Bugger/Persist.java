/*
Write a function, persistence, that takes in a positive parameter num
and returns its multiplicative persistence, which is the number of times
you must multiply the digits in num until you reach a single digit.

        For example:

        persistence(39) == 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
        // and 4 has only one digit

        persistence(999) == 4 // because 9*9*9 = 729, 7*2*9 = 126,
        // 1*2*6 = 12, and finally 1*2 = 2

        persistence(4) == 0 // because 4 is already a one-digit number
*/

import static java.util.Arrays.stream;

/*
public class Persist {
    public static int persistence(long n) {
        return n % 10 == n ? 0 : 1 + persistence(stream(("" + n).split("")).mapToInt(Integer::valueOf)
                .reduce(1, (a, b) -> a * b)
        );
    }
}*/

/*
public class Persist {
    public static int persistence(long n) {
        return n < 10 ? 0 : 1 + persistence(("" + n).chars().reduce(1, (a, b) -> a * (b - '0')));
    }
}
*/

public class Persist {
    public static int persistence(long n) {
        int count = 0;
        while (n >= 10) {
            n = ("" + n).chars().reduce(1, (a, b) -> a * (b - '0'));
            count++;
        }
        return count;
    }
}
