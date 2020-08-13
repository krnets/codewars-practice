/*
Create function fib that returns n'th element of Fibonacci sequence (classic programming task).
*/

import java.util.stream.Stream;

/*
public class Fibonacci {
    public static long fib(int n) {
        long a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            long temp = b;
            b = a + b;
            a = temp;
        }
        return a;
    }
}*/
public class Fibonacci {
    public static long fib(int n) {
        long a = 0, b = 1, temp;
        for (int i = 0; i < n; i++) {
            temp = b;
            b = a + b;
            a = temp;
        }
        return a;
    }
}
/*
public class Fibonacci {
    public static long fib(int n) {
        return Stream.iterate(new long[]{0, 1},
                i -> new long[]{i[1], i[0] + i[1]})
                .skip(n)
                .findFirst()
                .get()[0];
//                .orElse(new long[1])[0];
    }
}
*/
