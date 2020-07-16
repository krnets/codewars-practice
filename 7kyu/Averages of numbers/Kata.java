/*
Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.

        Example:

        Input:  [ 1, 3, 5, 1, -10]
        Output:  [ 2, 4, 3, -4.5]

        If the array has 0 or 1 values or is null or None, your method should return an empty array.
*/
/*

public class Kata {
    public static double[] averages(int[] numbers) {
        if (numbers == null || numbers.length <= 1)
            return new double[]{};
        var result = new double[numbers.length - 1];
        for (int i = 0; i < numbers.length - 1; i++)
            result[i] = (double) (numbers[i] + numbers[i + 1]) / 2;
        return result;
    }
}*/
/*
public class Kata {
    public static double[] averages(int[] numbers) {
        final double[] result = new double[(numbers == null || numbers.length <= 1) ? 0 : numbers.length - 1];
        for (int i = 0; i < result.length; i++)
            result[i] = (numbers[i] + numbers[i + 1]) / 2.0;
        return result;
    }
}
*/

/*
import java.util.stream.IntStream;

public class Kata {
    public static double[] averages(int[] numbers) {
        return numbers == null || numbers.length <= 1 ? new double[0] :
                IntStream.range(0, numbers.length - 1)
                        .mapToDouble(i -> (numbers[i] + numbers[i + 1]) / 2.0)
                        .toArray();
    }
}
*/
import static java.util.stream.IntStream.range;

public class Kata {
    public static double[] averages(int[] numbers) {
        return numbers == null ? new double[0] :
                range(0, numbers.length - 1).mapToDouble(i -> (numbers[i] + numbers[i + 1]) / 2.0).toArray();
    }
}
