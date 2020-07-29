/*
Create a function isDivisible(n,...) that checks if the first agrument n is divisible
by all other arguments (return true if no other arguments)

Example:
        isDivisible(6,1,3)--> true because 6 is divisible by 1 and 3
        isDivisible(12,2)--> true because 12 is divisible by 2
        isDivisible(100,5,4,10,25,20)--> true
        isDivisible(12,7)--> false because 12 is not divisible by 7
*/

import java.util.Arrays;
import java.util.stream.IntStream;

/*
public class Divisible {
    public static boolean isDivisible(int... nums) {
        return IntStream.range(1, nums.length)
                .allMatch(i -> nums[i] != 0 && nums[0] % nums[i] == 0);
    }
}
*/
/*
public class Divisible {
    public static boolean isDivisible(int... nums) {
        return nums.length < 2 || Arrays.stream(nums).skip(1).allMatch(v -> v != 0 && nums[0] % v == 0);
    }
}
*/
public class Divisible {
    public static boolean isDivisible(int... nums) {
        for (int x : nums)
            if (x == 0 || nums[0] % x != 0)
                return false;
        return true;
    }
}
