/*
The word i18n is a common abbreviation of internationalization in the developer community,
used instead of typing the whole word and trying to spell it correctly.
Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below)
within that string of length 4 or greater into an abbreviation, following these rules:

A "word" is a sequence of alphabetical characters.
By this definition, any other character like a space or hyphen (eg. "elephant-ride")
will split up a series of letters into two words (eg. "elephant" and "ride").

The abbreviated version of the word should have the first letter, then the number
of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

Example

        abbreviate("elephant-rides are really fun!")
        //          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*

        // words (^):   "elephant" "rides" "are" "really" "fun"
        //                123456     123     1     1234     1
        // ignore short words:               X              X

        // abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
        //                     "-"      " "    " "     " "     "!"
        // all non-word characters (*) remain in place
        === "e6t-r3s are r4y fun!"
*/

/*
import java.util.regex.Pattern;

public class Abbreviator {
    public String abbreviate(String string) {
        return Pattern.compile("\\B\\w{2,}\\B")
                .matcher(string)
                .replaceAll(m -> String.valueOf(m.group().length()));
    }
}
*/

public class Abbreviator {
    public String abbreviate(String string) {
        for (String s : string.split("[^a-zA-Z]"))
            if (s.length() > 3)
                string = string.replaceFirst(s, s.charAt(0) + (s.length() - 2 + s.substring(s.length() - 1)));

        return string;
    }
}
