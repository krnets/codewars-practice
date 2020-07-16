/*
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
*/

/*
public class MostDigits {
    public static int findLongest(int[] numbers) {
        int indexLongest = 0;
        for (int i = 0; i < numbers.length; i++)
            if (String.valueOf(numbers[i]).length() > String.valueOf(numbers[indexLongest]).length())
                indexLongest = i;
        return numbers[indexLongest];
    }
}
*/

import java.util.stream.IntStream;

/*
public class MostDigits {
    public static int findLongest(int[] numbers) {
        return IntStream.of(numbers)
                .reduce(0, (a, b) -> String.valueOf(Math.abs(a)).length() >= String.valueOf(Math.abs(b)).length() ? a : b);
    }
}
*/

import static java.util.stream.IntStream.of;

public class MostDigits {
    public static int findLongest(int[] numbers) {
        return of(numbers).reduce(0, (a, b) -> (Math.abs(a) + "").length() >= (Math.abs(b) + "").length() ? a : b);
    }
}
