/*
A Tidy number is a number whose digits are in non-decreasing order.

Task:  Given a number, Find if it is Tidy or not .
*/

/*
import java.util.stream.IntStream;

public class Solution {
    public static boolean tidyNumber(int number) {
        var strNum = String.valueOf(number).toCharArray();
        return IntStream.range(1, strNum.length)
                .allMatch(i -> Integer.parseInt(String.valueOf(strNum[i - 1])) <= Integer.parseInt(String.valueOf(strNum[i])));
    }
}*/

/*
public class Solution {
    public static boolean tidyNumber(int number) {
        return String.valueOf(number).matches("1*2*3*4*5*6*7*8*9*");
    }
}
*/

import java.util.Arrays;
import java.util.stream.Collectors;

import static java.lang.Integer.*;
import static java.util.stream.Stream.of;

/*
public class Solution {
    public static boolean tidyNumber(int number) {
        return number == parseInt(of(Integer.toString(number).split("")).sorted().collect(Collectors.joining()));
//        return number == parseInt(of(String.valueOf(number).split("")).sorted().collect(Collectors.joining()));
    }
}
*/

public class Solution {
    public static boolean tidyNumber(int number) {
        var strNum = Integer.toString(number).toCharArray();
        Arrays.sort(strNum);
        return number == Integer.parseInt(String.valueOf(strNum));
    }
}

/*
public class Solution {
    public static boolean tidyNumber(int number) {
        var strNum = String.valueOf(number).split("");
        Arrays.sort(strNum);
        return String.valueOf(number).equals(String.join("", strNum));
    }
}
*/
