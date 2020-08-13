/*
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

spinWords( "Hey fellow warriors" ) => "Hey wollef sroirraw"
spinWords( "This is a test") => "This is a test"
spinWords( "This is another test" ) => "This is rehtona test"
*/

import static java.util.Arrays.stream;
import static java.util.stream.Collectors.joining;

public class SpinWords {
    public String spinWords(String sentence) {
        return stream(sentence.split(" "))
                .map(word -> word.length() < 5 ? word : new StringBuilder(word).reverse().toString())
                .collect(joining(" "));
    }
}

/*
public class SpinWords {
    public String spinWords(String sentence) {
        var words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            if (words[i].length() >= 5)
                words[i] = new StringBuilder(words[i]).reverse().toString();
        }
        return String.join(" ", words);
    }
}
*/
