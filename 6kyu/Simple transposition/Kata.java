/*
Simple transposition is a basic and simple cryptography technique.
We make 2 rows and put first a letter in the Row 1,
the second in the Row 2,
third in Row 1 and so on until the end.

Then we put the text from Row 2 next to the Row 1 text and thats it.

Complete the function that receives a string and encrypt it with this simple transposition.

For example if the text to encrypt is: "Simple text", the 2 rows will be:

        Row 1 	S 	m 	l 		e 	t
        Row 2 	i 	p 	e 	t 	x

        So the result string will be: `"Sml etipetx"`
*/

/*
public class Kata {
    public static String simpleTransposition(String text) {
        var row1 = new StringBuilder();
        var row2 = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            if (i % 2 == 0)
                row1.append(text.charAt(i));
            else row2.append(text.charAt(i));
        }
        return row1.append(row2).toString();
    }
}
*/


import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.*;

public class Kata {
    public static String simpleTransposition(String text) {
        var row1 = range(0, text.length()).filter(i -> i % 2 == 0);
        var row2 = range(0, text.length()).filter(i -> i % 2 != 0);

        return concat(row1, row2).mapToObj(i -> text.substring(i, i + 1)).collect(joining());
    }
}
