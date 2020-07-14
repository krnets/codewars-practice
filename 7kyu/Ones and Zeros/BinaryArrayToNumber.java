/*
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

        Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

        Examples:

        Testing: [0, 0, 0, 1] ==> 1
        Testing: [0, 0, 1, 0] ==> 2
        Testing: [0, 1, 0, 1] ==> 5
        Testing: [1, 0, 0, 1] ==> 9
        Testing: [0, 0, 1, 0] ==> 2
        Testing: [0, 1, 1, 0] ==> 6
        Testing: [1, 1, 1, 1] ==> 15
        Testing: [1, 0, 1, 1] ==> 11

        However, the arrays can have varying lengths, not just limited to 4.
*/


import java.util.List;

/*
public class BinaryArrayToNumber {
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        StringBuilder result = new StringBuilder();
        for (int x : binary)
            result.append(String.valueOf(x));
        return Integer.parseInt(String.valueOf(result), 2);
    }
}
*/
/*
public class BinaryArrayToNumber {
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        int n = 0;
        for (int bit : binary)
            n = n << 1 | bit;
        return n;
    }
}*/
/*
public class BinaryArrayToNumber {
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        var sbNums = new StringBuilder();
        for (int bit : binary)
            sbNums.append(bit);
        return Integer.parseInt(sbNums.toString(), 2);
    }
}
*/
public class BinaryArrayToNumber {
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        return binary.stream().reduce((acc, val) -> acc * 2 + val).get();
    }
}
