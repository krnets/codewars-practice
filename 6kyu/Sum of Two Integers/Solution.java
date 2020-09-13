/*
Given Two integers a , b , find The sum of them ,
BUT You are not allowed to use the operators + and -

Notes:
        The numbers (a,b) may be positive , negative values or zeros .

        Returning value will be an integer .

        Java: the following methods are prohibited:
        addExact, average, collect, decrement, increment, nextAfter, nextDown, nextUp,
        reduce, subtractExact, sum, summing.

        The following classes are prohibited: BigDecimal and BigInteger .

        Input >> Output Examples

        1- Add (5,19) ==> return (24)

        2- Add (-27,18) ==> return (-9)

        3- Add (-14,-16) ==> return (-30)
*/

/*
public class Solution {
    public static int add(int x, int y) {
        while (y != 0) {
            int carry = x & y;
            x = x ^ y;
            y = carry << 1;
        }
        return x;
    }
}
*/


/*
public class Solution {
    public static int add(int x, int y) {
        return x \u002b y;
    }
}
*/

/*
public class Solution {
    public static int add(int x, int y) {
        return (int) Math.round(Math.log(Math.pow(1.0000001, x) * Math.pow(1.0000001, y)) / Math.log(1.0000001));
    }
}*/

public class Solution {
    public static int add(int x, int y) {
        return y == 0 ? x : add(x ^ y, (x & y) << 1);
    }
}
