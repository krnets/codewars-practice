import java.util.Arrays;
import java.util.stream.IntStream;

/*
Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:

        If the number has an integer square root, take this, otherwise square the number.
        [4,3,9,7,2,1] -> [2,9,3,49,4,1]

        The input array will always contain only positive numbers and will never be empty or null.
        The input array should not be modified!
*/
/*
public class Kata {
    public static int[] squareOrSquareRoot(int[] array) {
        int[] result = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            double squareRoot = Math.sqrt(array[i]);
            if (squareRoot % 1 == 0)
                result[i] = (int) squareRoot;
            else
                result[i] = (int) Math.pow(array[i], 2);
        }
        return result;
    }
}*/
public class Kata {
    public static int[] squareOrSquareRoot(int[] array) {
        return IntStream.of(array).map(v -> Math.sqrt(v) % 1 == 0 ? (int) Math.sqrt(v) : v * v).toArray();
    }
}
