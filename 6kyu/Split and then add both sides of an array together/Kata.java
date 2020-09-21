/*
You will receive an array as parameter that contains 1 or more integers and a number n.

Here is a little visualization of the process:

        Step 1: Split the array in two:

        [1, 2, 5, 7, 2, 3, 5, 7, 8]
        /            \
        [1, 2, 5, 7]    [2, 3, 5, 7, 8]

        Step 2: Put the arrays on top of each other:

           [1, 2, 5, 7]
        [2, 3, 5, 7, 8]

        Step 3: Add them together:

        [2, 4, 7, 12, 15]

        Repeat the above steps n times or until there is only one number left, and then return the array.

Example

        Input: arr=[4, 2, 5, 3, 2, 5, 7], n=2


        Round 1
        -------
        step 1: [4, 2, 5]  [3, 2, 5, 7]

        step 2:    [4, 2, 5]
        [3, 2, 5, 7]

        step 3: [3, 6, 7, 12]


        Round 2
        -------
        step 1: [3, 6]  [7, 12]

        step 2:  [3,  6]
        [7, 12]

        step 3: [10, 18]


        Result: [10, 18]
*/

import java.util.Arrays;

/*
public class Kata {
    public static int[] splitAndAdd(int[] numbers, int n) {
        if (numbers.length > 0 && n > 0) {
            int[] half = Arrays.copyOfRange(numbers, numbers.length / 2, numbers.length);

            for (int i = 0; i < numbers.length / 2; i++) {
                if (numbers.length % 2 == 0)
                    half[i] += numbers[i];
                else
                    half[i + 1] += numbers[i];
            }
            return splitAndAdd(half, n - 1);
        }
        return numbers;
    }
}
*/

/*
public class Kata {
    public static int[] splitAndAdd(int[] numbers, int n) {
        if (numbers.length > 0 && n > 0) {
            int[] half = Arrays.copyOfRange(numbers, numbers.length / 2, numbers.length);

            for (int i = 0; i < numbers.length / 2; i++) {
                half[i + numbers.length % 2] += numbers[i];
            }
            return splitAndAdd(half, n - 1);
        }
        return numbers;
    }
}
*/

public class Kata {
    public static int[] splitAndAdd(int[] numbers, int n) {
        if (numbers.length == 1 || n == 0) {
            return numbers;
        }
        int[] half = Arrays.copyOfRange(numbers, numbers.length / 2, numbers.length);

        for (int i = 0; i < numbers.length / 2; i++) {
            half[i + numbers.length % 2] += numbers[i];
        }
        return splitAndAdd(half, n - 1);
    }
}

/*
public class Kata {
    public static int[] splitAndAdd(int[] numbers, int n) {
        int[] arr = Arrays.copyOf(numbers, numbers.length);

        while (arr.length > 1 && n > 0) {
            int[] temp = Arrays.copyOfRange(arr, arr.length / 2, arr.length);

            for (int i = 0; i < arr.length / 2; i++) {
                temp[i + arr.length % 2] += arr[i];
            }

            arr = temp;
            n--;
        }
        return arr;
    }
}
*/
