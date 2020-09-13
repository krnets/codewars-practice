/*
Given a lowercase string that has alphabetic characters only and no spaces,
return the highest value of consonant substrings.
Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values:
a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

        -- The consonant substrings are:
        "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22.
        The highest is 26.
        solve("zodiacs") = 26

        For the word "strength", solve("strength") = 57
        -- The consonant substrings are:
        "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49.
        The highest is 57.
*/

/*
import java.util.ArrayList;
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ConsonantValue {
    public static int solve(final String s) {
        var splitOnVowels = s.split("[aeiou]");

        var alphabet = IntStream.range(0, 26)
                .mapToObj(i -> Character.toString('a' + i))
                .collect(Collectors.joining());

        var values = new ArrayList<Integer>();

        for (String x : splitOnVowels) {
            int val = 0;

            for (int i = 0; i < x.length(); i++)
                val += alphabet.indexOf(x.charAt(i)) + 1;

            values.add(val);
        }
        return values.stream().max(Comparator.naturalOrder()).orElse(0);
    }
}
*/

import java.util.Arrays;

public class ConsonantValue {
    public static int solve(final String s) {
        return Arrays.stream(s.split("[aeiou]"))
                .mapToInt(consonants -> consonants.chars().map(c -> c - ('a' - 1)).sum())
                .max().orElse(0);
    }
}
