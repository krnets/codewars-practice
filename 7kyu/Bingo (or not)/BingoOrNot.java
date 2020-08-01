/*
For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input.
Duplicate numbers within the array are possible.

Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc).
Write a function where you will win the game if your numbers can spell "BINGO".
They do not need to be in the right order in the input array). Otherwise you will lose.
Your outputs should be "WIN" or "LOSE" respectively.
*/

//package com.codewars.julesnuggy;


/*
public class BingoOrNot {
    public static String bingo(int[] numberArray){
        var BINGO = new ArrayList<Integer>();

        for (char c : "BINGO".toCharArray())
            BINGO.add(((int) c) - 64);
        var x =

        var result = BINGO.stream().allMatch(v -> Arrays.stream(numberArray).findAny(v));



        return result ? "WIN" : "LOSE";
    }
}
*/

import java.util.Arrays;
import java.util.stream.Collectors;

public class BingoOrNot {
    public static String bingo(int[] numberArray) {
        var nums = Arrays.stream(numberArray).boxed().collect(Collectors.toList());
        return "BINGO".chars().map(i -> i - 64).allMatch(nums::contains) ? "WIN" : "LOSE";
    }
}

/*
import static java.util.Arrays.stream;
import static java.util.stream.Collectors.*;

public class BingoOrNot {
    public static String bingo(int[] numberArray) {
        return stream(numberArray).boxed().collect(toList())
                .containsAll("BINGO".chars().map(i -> i - 64).boxed().collect(toList())) ? "WIN" : "LOSE";
    }
}
*/

