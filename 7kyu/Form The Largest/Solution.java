/*
Given a number , Return The Maximum number  could be formed from the digits of the number given .
Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive !alt !alt
Digit Duplications could occur , So also consider it when forming the Largest !alt

        Input >> Output Examples:

        maxNumber (213) ==> return (321)
        Explanation:
        As 321 is The Maximum number  could be formed from the digits of the number *213*** .

        maxNumber (7389) ==> return (9873)
        Explanation:
        As 9873 is The Maximum number  could be formed from the digits of the number *7389*** .

        maxNumber (63729) ==> return (97632)
        Explanation:
        As 97632 is The Maximum number could be formed from the digits of the number *63729*** .

        maxNumber (566797) ==> return (977665)
        Explanation:
        As 977665 is The Maximum number could be formed from the digits of the number *566797*** .

        Note : Digit duplications are considered when forming the largest .

        maxNumber (17693284) ==> return (98764321)
        Explanation:
        As 98764321 is _The Maximum number _ could be formed from the digits of the number *17693284*** .
*/

/*
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;

public class Solution {
    public static long maxNumber(long n) {
        return Long.parseLong(
                Arrays.stream(String.valueOf(n).split(""))
                        .sorted(Comparator.reverseOrder())
                        .collect(Collectors.joining())
        );
    }
}*/


import static java.lang.Long.parseLong;
import static java.util.Arrays.stream;
import static java.util.Comparator.reverseOrder;
import static java.util.stream.Collectors.joining;

public class Solution {
    public static long maxNumber(long n) {
        return parseLong(stream(String.valueOf(n).split("")).sorted(reverseOrder()).collect(joining()));
    }
}
