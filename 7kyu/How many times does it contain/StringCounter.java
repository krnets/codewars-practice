/*
Your task is to return how many times a string contains a given character.

The function takes a string(inputS) as a paremeter and a char(charS)
which is the character that you will have to find and count.

For example, if you get an input string "Hello world" and the character to find is "o", return 2.
*/

public class StringCounter {
    public static int stringCounter(String inputS, char charS) {
        return inputS.replaceAll("[^" + charS + "]", "").length();
    }
}