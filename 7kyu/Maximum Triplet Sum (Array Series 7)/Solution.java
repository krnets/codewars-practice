/*
Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

Notes : Array/list size is at least 3 .
        Array/list numbers could be a mixture of positives , negatives and zeros .
        Repetition of numbers in the array/list could occur ,
        So (duplications are not included when summing).

Input >> Output Examples

        1- maxTriSum ({3,2,6,8,2,3}) ==> return (17)

        As the triplet that maximize the sum {6,8,3} in order , their sum is (17)
        Note : duplications are not included when summing , (i.e) the numbers added only once .

        2- maxTriSum ({2,1,8,0,6,4,8,6,2,4}) ==> return (18)

        As the triplet that maximize the sum {8, 6, 4} in order , their sum is (18) ,
        Note : duplications are not included when summing , (i.e) the numbers added only once .

        3- maxTriSum ({-7,12,-7,29,-5,0,-7,0,0,29}) ==> return (41)

        As the triplet that maximize the sum {12 , 29 , 0} in order , their sum is (41) ,
        Note : duplications are not included when summing , (i.e) the numbers added only once .
*/

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.stream.IntStream;

/*
public class Solution {
    public static int maxTriSum(int[] numbers) {
        var uniqueNums = new HashSet<Integer>();
        for (int num : numbers) {
            uniqueNums.add(num);
        }
        var arr = uniqueNums.stream().mapToInt(i -> i).toArray();
        Arrays.sort(arr);
        return IntStream.of(arr).skip(arr.length - 3).sum();
    }
}
*/

/*
public class Solution {
    public static int maxTriSum(int[] numbers) {
        var set = new HashSet<Integer>();
        for (int num : numbers) {
            set.add(num);
        }
//        return set.stream().sorted(Comparator.reverseOrder()).limit(3).reduce(0, (a, b) -> a + b);
        return set.stream().sorted(Comparator.reverseOrder()).limit(3).mapToInt(i -> i).sum();
    }
}

*/

public class Solution {
    public static int maxTriSum(int[] numbers) {
        return Arrays.stream(numbers).boxed().distinct()
                .sorted(Comparator.reverseOrder())
                .limit(3).mapToInt(i -> i)
                .sum();
    }
}
