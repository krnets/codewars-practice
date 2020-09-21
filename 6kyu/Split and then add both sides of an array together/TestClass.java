import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

import java.util.*;

public class TestClass {

    Random r = new Random();

    @Test
    public void splitAndAddTest() throws Exception {

        int[] expected = new int[]{5, 10};
        int[] input = Kata.splitAndAdd(new int[]{1, 2, 3, 4, 5}, 2);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{15};
        input = Kata.splitAndAdd(new int[]{1, 2, 3, 4, 5}, 3);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{4, 6};
        input = Kata.splitAndAdd(new int[]{1, 2, 3, 4}, 1);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{21};
        input = Kata.splitAndAdd(new int[]{1, 2, 3, 4, 5, 6}, 20);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{15};
        input = Kata.splitAndAdd(new int[]{15}, 3);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{183, 125};
        input = Kata.splitAndAdd(new int[]{32, 45, 43, 23, 54, 23, 54, 34}, 2);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{32, 45, 43, 23, 54, 23, 54, 34};
        input = Kata.splitAndAdd(new int[]{32, 45, 43, 23, 54, 23, 54, 34}, 0);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{305, 1195};
        input = Kata.splitAndAdd(new int[]{3, 234, 25, 345, 45, 34, 234, 235, 345}, 3);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));

        expected = new int[]{1040, 7712};
        input = Kata
                .splitAndAdd(new int[]{3, 234, 25, 345, 45, 34, 234, 235, 345, 34, 534, 45, 645, 645, 645, 4656, 45, 3}, 4);

        assertEquals(Arrays.toString(expected), Arrays.toString(input));


    }

    @Test
    public void randTest() throws Exception {

        for (int i = 0; i <= 10; i++) {

            int[] randomArr = generateRandomArr();
            int iterations = r.nextInt(5) + 1;
            assertEquals(Arrays.toString(splitAndAdd(randomArr, iterations)), Arrays
                    .toString(Kata.splitAndAdd(randomArr, iterations)));

        }


    }


    private int[] generateRandomArr() {

        int[] toReturn = new int[r.nextInt(100) + 1];

        for (int i = 0; i < toReturn.length; i++) {
            toReturn[i] = r.nextInt(100);
        }

        return toReturn;
    }


    public static int[] splitAndAdd(int[] numbers, int n) {
        if (numbers.length == 1 || n == 0) return numbers;
        return splitAndAdd(addBothSidesTogether(numbers), n - 1);
    }

    private static int[] addBothSidesTogether(int[] arr) {

        boolean evenLength = arr.length % 2 == 0;
        int[] added = new int[evenLength ? arr.length / 2 : arr.length / 2 + 1];

        if (!evenLength) {
            int middleNumber = arr[arr.length / 2];
            added[0] = middleNumber;
        }

        int[] left = getLeftSide(arr);
        int[] right = getRightSide(arr, evenLength);

        for (int i = evenLength ? 0 : 1, j = 0; i < added.length; i++, j++) {
            added[i] = left[j] + right[j];
        }

        return added;

    }


    private static int[] getRightSide(int[] arr, boolean evenLength) {
        if (evenLength) return Arrays.copyOfRange(arr, arr.length / 2, arr.length);
        else return Arrays.copyOfRange(arr, arr.length / 2 + 1, arr.length);
    }

    private static int[] getLeftSide(int[] arr) {
        return Arrays.copyOfRange(arr, 0, arr.length / 2);
    }


}