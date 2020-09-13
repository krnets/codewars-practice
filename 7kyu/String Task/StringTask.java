/*
Petya started to attend programming lessons.
On the first lesson his task was to write a simple program.
The program was supposed to do the following:
in the given string, consisting of uppercase and lowercase Latin letters, it:

        deletes all the vowels,
        inserts a character "." before each consonant,
        replaces all uppercase consonants with corresponding lowercase ones.

Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants.
The program's input is exactly one string, it should return the output as a single string,
resulting after the program's processing the initial string.

Input:  The first argument represents input string of Petya's program.
        This string only consists of uppercase and lowercase Latin letters.

Output: Return the resulting string.

Examples:
        ('tour')      =>  '.t.r'
        ('Codewars')  =>  '.c.d.w.r.s'
        ('aBAcAba')   =>  '.b.c.b'
*/

public class StringTask {
    public static String perform(String word) {
        var vowels = "aeiouy";
        var consonants = new StringBuilder();

        for (char c : word.toLowerCase().toCharArray()) {
            var s = Character.toString(c);
            if (!vowels.contains(s))
                consonants.append(".").append(s);
        }
        return consonants.toString();
    }
}

/*
import java.util.Set;

public class StringTask {
    public static String perform(String word) {
        var vowels = Set.of("a", "e", "i", "o", "u", "y");
        var consonants = new StringBuilder();

        for (char c : word.toLowerCase().toCharArray()) {
            var s = Character.toString(c);
            if (!vowels.contains(s))
                consonants.append(".").append(s);
        }
        return consonants.toString();
    }
}
*/

/*
import java.util.Arrays;

import static java.util.function.Predicate.not;
import static java.util.stream.Collectors.joining;

public class StringTask {
    public static String perform(String word) {
        String vowels = "aeiouy";

        return Arrays.stream(word.toLowerCase().split(""))
                .filter(not(vowels::contains))
                .map(c -> "." + c)
                .collect(joining());
    }
}

*/
/*
public class StringTask {
    public static String perform(String word) {
        String vowels = "[aeiouy]";

        return word.toLowerCase()
                .replaceAll(vowels, "")
                .replaceAll("(.)", ".$0");
    }
}
*/
