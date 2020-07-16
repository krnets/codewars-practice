/*
Given an integer as input, can you round it to the next (meaning, "higher") 5?

        Examples:

        input:    output:
        0    ->   0
        2    ->   5
        3    ->   5
        12   ->   15
        21   ->   25
        30   ->   30
        -2   ->   0
        -5   ->   -5
        etc.

        Input may be any positive or negative integer (including 0).

        You can assume that all inputs are valid integers.
*/

/*
public class RoundToTheNextMultipleOf5 {
    public static int roundToNext5(int number) {
        return (int) (Math.ceil(number / 5.0) * 5);
    }
}
*/
/*
public class RoundToTheNextMultipleOf5 {
    public static int roundToNext5(int number) {
        while (number % 5 != 0)
            number++;
        return number;
    }
}
*/
public class RoundToTheNextMultipleOf5 {
    public static int roundToNext5(int number) {
        if (number % 5 == 0)
            return number;
        return roundToNext5(++number);
    }
}