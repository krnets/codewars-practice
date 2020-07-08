/*
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
Assume input will be only of Integer or String type
*/

import java.util.List;

public class MixedSum {
    public int sum(List<?> mixed) {
        return mixed.stream().mapToInt(o -> Integer.parseInt(o.toString())).sum();
    }
}
/*

public class MixedSum {
    public int sum(List<?> mixed) {
        int result = 0;
        for (Object o : mixed)
            result += Integer.parseInt(o.toString());
        return result;
    }
}
*/
