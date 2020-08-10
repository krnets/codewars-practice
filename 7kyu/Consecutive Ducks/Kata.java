/*
Positive integers have so many gorgeous features.
Some of them could be expressed as a sum of two or more consecutive positive numbers.

Consider an Example :

        10 , could be expressed as a sum of 1 + 2 + 3 + 4.

Task  : Given Positive integer N
        return true if it could be expressed as a sum of two or more consecutive positive numbers
        otherwise return false.

Notes : Guaranteed constraint : 2 ≤ N ≤ (2^31) -1 .

Input >> Output Examples:


* consecutiveDucks(9)  ==>  return (true)  //  9 , could be expressed as a sum of ( 2 + 3 + 4 ) or ( 4 + 5 ) .

* consecutiveDucks(64)  ==>  return (false)

* consecutiveDucks(42)  ==>  return (true) //  42 , could be expressed as a sum of ( 9 + 10 + 11 + 12 )  .
*/


/*
public class Kata {
    public static boolean consecutiveDucks(int n) {
        return Math.log(n) / Math.log(2) % 1 != 0;
    }
}*/

/*
public class Kata {
    public static boolean consecutiveDucks(int n) {
        return Integer.bitCount(n) > 1;
    }
}
*/

public class Kata {
    public static boolean consecutiveDucks(int n) {
        return (n-- & n) > 0;
    }
}
