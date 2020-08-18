/*
Write simple .camelCase method for strings.
All words must have their first letter capitalized without spaces.

        camelCase("hello case"); // => "HelloCase"
        camelCase("camel case word"); // => "CamelCaseWord"
*/

/*
import static java.util.Arrays.stream;
import static java.util.function.Predicate.not;

public class Solution {
    public static String camelCase(String str) {
        return stream(str.split(" "))
                .filter(not(String::isEmpty))
                .reduce("", (a, b) -> a + b.substring(0, 1).toUpperCase() + b.substring(1));
    }
}
*/

import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
public class Solution {
    public static String camelCase(String str) {
        return str.isEmpty() ? "" : of(str.trim().split("\\s+"))
                .reduce("", (a, b) -> a + b.substring(0, 1).toUpperCase() + b.substring(1));
    }
}
*/
public class Solution {
    public static String camelCase(String str) {
        return str.isEmpty() ? "" : Stream.of(str.trim().split("\\s+"))
                .map(word -> word.substring(0, 1).toUpperCase().concat(word.substring(1)))
                .collect(Collectors.joining());
    }
}
