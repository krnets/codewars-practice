/*
You are going to be given an array of integers.
Your job is to take that array and find an index N
where the sum of the integers to the left of N
is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array,
the sum of left side of the index ({1,2,3})
and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array,
the sum of left side of the index ({1})
and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
        You are given the array {20,10,-80,10,10,15,35}
        At index 0 the left side is {}
        The right side is {10,-80,10,10,15,35}
        They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
        Index 0 is the place where the left side and right side are equal.

Input:  An integer array of length 0 < arr < 1000.
        The numbers in the array can be any integer positive or negative.

Output: The lowest index N where the side to the left of N is equal
        to the side to the right of N. If you do not find an index
        that fits these rules, then you will return -1.

Note:   If you are given an array with multiple answers, return the lowest correct index.
*/

import static java.util.Arrays.stream;

/*
public class Kata {
    public static int findEvenIndex(int[] arr) {
        int sumTotal = stream(arr).sum();
        int leftSum = 0;
        for (int i = 0; i < arr.length; i++) {
            sumTotal -= arr[i];
            if (leftSum == sumTotal)
                return i;
            leftSum += arr[i];
        }
        return -1;
    }
}
*/
public class Kata {
    public static int findEvenIndex(int[] arr) {
        int rightSum = stream(arr).sum();
        int leftSum = 0;
        for (int i = 0; i < arr.length; i++) {
            rightSum -= arr[i];
            if (leftSum == rightSum)
                return i;
            leftSum += arr[i];
        }
        return -1;
    }
}

/*
import static java.util.stream.IntStream.*;

public class Kata {
    public static int findEvenIndex(int[] arr) {
        return range(0, arr.length)
                .filter(i -> of(arr).limit(i).sum() == of(arr).skip(i + 1).sum())
                .findFirst().orElse(-1);
    }
}
*/
