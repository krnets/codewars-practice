/*
Given a string, you need to write a method that order every letter in this string in ascending order.

Also, you should validate that the given string is not empty or null.
If so, the method should return:
        "Invalid String!"

Notes
        • the given string can be lowercase and uppercase.
        • the string could include spaces or other special characters like '# ! or ,'

Examples
        "hello world" => " dehllloorw"
        "bobby"       => "bbboy"
        ""            => "Invalid String!"
        "!Hi You!"    => " !!HYiou"
*/

import static java.util.stream.Collectors.*;

public class Ordering {
    public String orderWord(String s) {
        return s == null || s.isEmpty() ? "Invalid String!" :
                s.chars().sorted().mapToObj(Character::toString).collect(joining());
    }
}