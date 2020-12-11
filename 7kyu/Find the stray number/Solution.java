/*
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

        Complete the method which accepts such an array, and returns that single different number.

        The input array will always be valid! (odd-length >= 3)
        Examples

        [1, 1, 2] ==> 2
        [17, 17, 3, 17, 17, 17, 17] ==> 3
*/

import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    static int stray(int[] numbers) {
        return IntStream.of(numbers).reduce((prev, curr) -> prev ^ curr).getAsInt();
    }
}

/*
class Solution {
    static int stray(int[] numbers) {
        return Arrays.stream(numbers).reduce(0, (prev, curr) -> prev ^ curr);
    }
}
*/
