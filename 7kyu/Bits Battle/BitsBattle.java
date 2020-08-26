/*
The odd and even numbers are fighting against each other!

You are given a list of positive integers.
The odd numbers from the list will fight using their 1 bits from their binary representation,
while the even numbers will fight using their 0 bits.
If present in the list, number 0 will be neutral, hence not fight for either side.

You should return:

        odds win if number of 1s from odd numbers is larger than 0s from even numbers
        evens win if number of 1s from odd numbers is smaller than 0s from even numbers
        tie if equal, including if list is empty

Please note that any prefix that might appear in the binary representation,
e.g. 0b, should not be counted towards the battle.

Example:

        For an input list of [5, 3, 14]:

        odds: 5 and 3 => 101 and 11 => four 1s
        evens: 14 => 1110 => one 0

        Result: odds win the battle with 4-1
*/

import java.util.ArrayList;
import java.util.Arrays;

/*
public class BitsBattle {
    static String bitsBattle(int[] numbers) {
        var odds = new ArrayList<String>();
        var evens = new ArrayList<String>();

        for (int n : Arrays.stream(numbers).filter(x -> x > 0).toArray()) {
            if (n % 2 == 0)
                evens.add(Integer.toBinaryString(n).replace("1", ""));
            else odds.add(Integer.toBinaryString(n).replace("0", ""));
        }
        var oddsLength = String.join("", odds).length();
        var evensLength = String.join("", evens).length();

        return oddsLength > evensLength ? "odds win" : oddsLength < evensLength ? "evens win" : "tie";
    }
}*/

/*
public class BitsBattle {
    static String bitsBattle(int[] numbers) {
        var nums = Arrays.stream(numbers).filter(x -> x > 0).toArray();
        var odds = new StringBuilder();
        var evens = new StringBuilder();

        for (int n : nums) {
            if (n % 2 == 0)
                evens.append(Integer.toBinaryString(n).replace("1", ""));
            else odds.append(Integer.toBinaryString(n).replace("0", ""));
        }
        var oddsLength = String.join("", odds).length();
        var evensLength = String.join("", evens).length();

        return oddsLength > evensLength ? "odds win" : oddsLength < evensLength ? "evens win" : "tie";
    }
}
*/

/*
public class BitsBattle {
    static String bitsBattle(int[] numbers) {
        int odds = 0, evens = 0;

        for (int n : numbers) {
            if (n == 0) continue;
            if (n % 2 == 0)
                evens += Integer.toBinaryString(n).replace("1", "").length();
            else odds += Integer.toBinaryString(n).replace("0", "").length();
        }
        return odds > evens ? "odds win" : odds < evens ? "evens win" : "tie";
    }
}
*/

public class BitsBattle {
    static String bitsBattle(int[] numbers) {
        int odds = 0, evens = 0;

        for (int n : numbers) {
            if (n == 0) continue;
            if (n % 2 == 0)
                evens += Integer.toBinaryString(n).length() - Integer.bitCount(n);
            else odds += Integer.bitCount(n);
        }
        return odds > evens ? "odds win" : odds < evens ? "evens win" : "tie";
    }
}
