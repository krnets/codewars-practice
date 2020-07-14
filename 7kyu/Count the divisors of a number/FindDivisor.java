/*
Count the number of divisors of a positive integer n.

        Random tests go up to n = 500000.
        Examples

        numberOfDivisors(4)  == 3 // 1, 2, 4
        numberOfDivisors(5)  == 2 // 1, 5
        numberOfDivisors(12) == 6 // 1, 2, 3, 4, 6, 12
        numberOfDivisors(30) == 8 // 1, 2, 3, 5, 6, 10, 15, 30
*/

import java.util.stream.IntStream;

/*
public class FindDivisor {
    public long numberOfDivisors(int n) {
        return IntStream.rangeClosed(1, n)
                .filter(i -> n % i == 0)
                .count();
    }
}*/

public class FindDivisor {
    public long numberOfDivisors(int n) {
        return n == 0 ? 0 : IntStream.rangeClosed(1, n / 2)
                .filter(i -> n % i == 0)
                .count() + 1;
    }
}
