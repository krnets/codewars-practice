import java.util.stream.IntStream;

/*
Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.

        summation(2) -> 3
        1 + 2

        summation(8) -> 36
        1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
*/
/*
public class GrassHopper {
    public static int summation(int n) {
        if (n == 0)
            return 0;
        return n + summation(n - 1);
    }
}*/
/*
public class GrassHopper {
    public static int summation(int n) {
        return n * (n + 1) / 2;
    }
}
*/
/*
public class GrassHopper {
    public static int summation(int n) {
        int sum = 0;
        for (int i = 0; i <= n; i++)
            sum += i;
        return sum;
    }
}
*/
public class GrassHopper {
    public static int summation(int n) {
        return IntStream.rangeClosed(0, n).sum();
    }
}
