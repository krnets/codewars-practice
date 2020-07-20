/*
Given a positive integer n, calculate the following sum:

        n + n/2 + n/4 + n/8 + ...

        All elements of the sum are the results of integer division.
        Example

        25  =>  25 + 12 + 6 + 3 + 1 = 47
*/
/*

public class HalvingSum {
    int halvingSum(int n) {
        int sum = 1;
        while (n > 1) {
            sum += n;
            n /= 2;
        }
        return sum;
    }
}*/

/*
public class HalvingSum {
    int halvingSum(int n) {
        return n > 1 ? n + halvingSum(n / 2) : 1;
    }
}
*/

import java.util.stream.IntStream;

/*
public class HalvingSum {
    int halvingSum(int n) {
        return IntStream.iterate(n, i -> i / 2).limit(n).sum();
    }
}
*/
public class HalvingSum {
    int halvingSum(int n) {
        return IntStream.iterate(n, i -> i > 0, i -> i / 2).sum();
    }
}
