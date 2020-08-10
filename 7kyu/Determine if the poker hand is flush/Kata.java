/*
Determine if the poker hand is flush, meaning if the five cards are of the same suit.

Your function will be passed a list/array of 5 strings, each representing a poker card
in the format "5H" (5 of hearts), meaning the value of the card followed by the initial of its suit
(Hearts, Spades, Diamonds or Clubs). No jokers included.

Your function should return true if the hand is a flush, false otherwise.

The possible card values are 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

Examples

        ["AS", "3S", "9S", "KS", "4S"]  ==> true

        ["AD", "4S", "7H", "KS", "10S"] ==> false
*/

import java.util.Arrays;

/*
public class Kata{
    public static boolean CheckIfFlush(String[] cards){
        return Arrays.stream(cards)
                .allMatch(v -> v.substring(v.length() - 1).equals(cards[0].substring(cards[0].length() - 1)));
    }
}*/
public class Kata {
    public static boolean CheckIfFlush(String[] cards) {
        return Arrays.stream(cards)
                .map(v -> v.substring(v.length() - 1))
                .distinct()
                .count() == 1;
    }
}
