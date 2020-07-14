/*
We want to generate a function that computes the series starting from 0 and ending until the given number.
        Example:

        Input:
        > 6

        Output:
        0+1+2+3+4+5+6 = 21

        Input:
        > -15

        Output:
        -15<0

        Input:
        > 0

        Output:
        0=0
*/
/*

public class SequenceSum {
    public static String showSequence(int value) {
        if (value == 0) return "0=0";
        if (value < 0) return value + "<0";
        int sum = 0;
        var result = new StringBuilder();
        for (int i = 0; i <= value; i++) {
            sum += i;
            result.append(i);
            result.append("+");
        }
        return result.substring(0, result.length() - 1) + " = " + sum;
    }
}*/

public class SequenceSum {
    public static String showSequence(int value) {
        if (value < 1)
            return value + (value == 0 ? "=0" : "<0");
        var seq = new StringBuilder();
        for (int i = 0; i <= value; i++)
            seq.append(i).append("+");
        return seq.deleteCharAt(seq.length() - 1).append(" = ").append(value * (value + 1) / 2).toString();
    }
}
