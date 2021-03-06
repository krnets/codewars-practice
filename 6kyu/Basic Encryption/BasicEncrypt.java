/*
The most basic encryption method is to map a char to another char by a certain math rule.
Because every char has an ASCII value, we can manipulate this value with a simple math expression.

For example 'a' + 1 would give us 'b', because 'a' value is 97 and 'b' value is 98.

You will need to write a method which does exactly that -

get a string as text and an int as the rule of manipulation, and should return encrypted text.

        encrypt("a",1) = "b"

Full ascii table is used on our question (256 chars) - so 0-255 are the valid values.
*/

import java.util.stream.Collectors;

public class BasicEncrypt {
    public String encrypt(String text, int rule) {
        return text.chars()
                .map(i -> (i + rule) % 256)
                .mapToObj(Character::toString)
                .collect(Collectors.joining());
    }
}