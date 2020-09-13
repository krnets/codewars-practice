/*
You get an array of different numbers to sum up.
But there is one problem, those numbers all have different bases. For example:

        You get an array of BasedNumbers as an input:

public class BasedNumbers{
    String number;
    int base;
}

    [{number:"101", base:16},
    {number:"7640", base:8},
    {number:"1", base:9}]

The output should be the sum as an integer value with a base of 10,
so according to the example this would be:

        4258

A few more examples:

        [{number:"101", base:2}, {number:"10", base:8}] --> 13
        [{number:"ABC", base:16}, {number:"11", base:2}] --> 2751

        Bases can be between 2 and 36 (2<=base<=36)
*/


/*
import java.util.ArrayList;

public class ArraySumminator {
    public static long sumItUp(BasedNumbers[] numbersWithBases) {
        var nums = new ArrayList<Integer>();

        for (BasedNumbers bn : numbersWithBases) {
            nums.add(Integer.parseInt(bn.number, bn.base));
        }
        return nums.stream().mapToInt(i -> i).sum();
    }
}*/

/*
public class ArraySumminator {
    public static long sumItUp(BasedNumbers[] numbersWithBases) {
        long sum = 0;

        for (BasedNumbers bn : numbersWithBases)
            sum += Integer.parseInt(bn.number, bn.base);

        return sum;
    }
}
*/

import java.util.Arrays;

public class ArraySumminator {
    public static long sumItUp(BasedNumbers[] numbersWithBases) {
        return Arrays.stream(numbersWithBases)
                .mapToInt(bn -> Integer.parseInt(bn.number, bn.base))
                .sum();
    }
}
