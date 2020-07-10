/*
Simple challenge - eliminate all bugs from the supplied code so that the code runs and
outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.
*/

import java.util.stream.Stream;

/*
public class Kata {
    public static int findLongest(final String str) {
        String[] words = str.split(" ");
        int longest = 0;
        for (int i = 0; i < words.length; i++)
            if (words[i].length() > longest)
                longest = words[i].length();
        return longest;
    }
}
*/
/*
public class Kata {
    public static int findLongest(final String str) {
        String[] words = str.split(" ");
        int longest = 0;
        for (String word : words)
            if (word.length() > longest)
                longest = word.length();
        return longest;
    }
}
*/
/*
public class Kata {
    public static int findLongest(final String str) {
        return Stream.of(str.split(" ")).mapToInt(word -> word.length()).max().getAsInt();
    }
}
*/
public class Kata {
    public static int findLongest(String str) {
        return Stream.of(str.split(" ")).mapToInt(String::length).max().getAsInt();
    }
}
