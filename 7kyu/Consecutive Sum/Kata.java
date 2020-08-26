/*
Let's say we have a number, num.
Find the number of values of n such that:
there exists n consecutive positive values that sum up to num.
A positive number is > 0.
n can also be 1.

//Examples
        int num = 1;
//1
        return 1;

        int num = 15;
//15, (7, 8), (4, 5, 6), (1, 2, 3, 4, 5)
        return 4;

        int num = 48;
//48, (15, 16, 17)
        return 2;

        int num = 97;
//97, (48, 49)
        return 2;

        The upper limit is 10^8
*/

import java.util.stream.IntStream;

public class Kata {
    public static int consecutiveSum(int num) {
        return (int) (1 + IntStream.rangeClosed(2, (int) Math.sqrt(2 * num))
                .filter(i -> ((2 * num) % i) == 0)
                .filter(i -> (((2 * num / i) - i) & 1) == 1)
                .count());
    }
}

/*
public class Kata {
    public static int consecutiveSum(int num) {
        int count = 0;
        num <<= 1;
        for (int i = 1; i * i < num; i++)
            if (num % i == 0 && ((i + num / i) & 1) == 1)
                count++;
        return count;
    }
}*/
