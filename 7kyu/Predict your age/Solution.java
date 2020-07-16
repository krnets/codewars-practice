/*
My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

        Take a list of ages when each of your great-grandparent died.
        Multiply each number by itself.
        Add them all together.
        Take the square root of the result.
        Divide by two.

        Example

        predictAge(65, 60, 75, 55, 60, 63, 64, 45) === 86

        Note: the result should be rounded down to the nearest integer.
*/

import java.util.stream.IntStream;
/*
public class Solution {
    public static int predictAge(int age1, int age2, int age3, int age4, int age5, int age6, int age7, int age8) {
        int[] ages = new int[]{age1, age2, age3, age4, age5, age6, age7, age8};
        return (int) Math.sqrt(IntStream.of(ages).map(v -> v * v).sum()) / 2;
    }
}*/
public class Solution {
    public static int predictAge(int...ages) {
        return (int) (Math.sqrt(IntStream.of(ages).map(v -> v * v).sum()) / 2);
    }
}
