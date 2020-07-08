import java.util.stream.IntStream;

/*
Get the number n (n>0) to return the reversed sequence from n to 1.

        Example : n=5 >> [5,4,3,2,1]
*/
/*
public class Sequence {
    public static int[] reverse(int n) {
        int[] range = IntStream.rangeClosed(1, n).toArray();
        int[] result = new int[n];
        for (int i = n - 1; i >= 0; i--)
            result[i] = range[n - i - 1];
        return result;
    }
}
*/
/*
public class Sequence {
    public static int[] reverse(int n) {
        int[] result = new int[n];
        for (int i = 0; i < n; i++)
            result[i] = n - i;
        return result;
    }
}
*/
/*
public class Sequence {
    public static int[] reverse(int n) {
        return IntStream.rangeClosed(-n, -1).map(Math::abs).toArray();
    }
}
*/
public class Sequence {
    public static int[] reverse(int n) {
        return IntStream.range(-n, 0).map(Math::abs).toArray();
    }
}
