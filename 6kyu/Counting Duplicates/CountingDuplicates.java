/*
Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string.

The input string can be assumed to contain only alphabets (both uppercase and lowercase)
and numeric digits.

        "abcde" -> 0 # no characters repeats more than once
        "aabbcde" -> 2 # 'a' and 'b'
        "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
        "indivisibility" -> 1 # 'i' occurs six times
        "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
        "aA11" -> 2 # 'a' and '1'
        "ABBA" -> 2 # 'A' and 'B' each occur twice
*/

import static java.util.stream.Collectors.*;

/*
public class CountingDuplicates {
    public static int duplicateCount(String text) {
        var counter = text.chars().boxed().collect(Collectors.groupingBy(c -> c, Collectors.counting()));
        return (int) counter.entrySet().stream().filter(e -> e.getValue() > 1).count();
    }
}*/

/*
public class CountingDuplicates {
    public static int duplicateCount(String text) {
        return (int) text.toLowerCase().chars().boxed()
                .collect(groupingBy(c -> c, counting()))
                .entrySet().stream()
                .filter(e -> e.getValue() > 1)
                .count();
    }
}
*/
/*
public class CountingDuplicates {
    public static int duplicateCount(String text) {
        return (int) text.toLowerCase().chars().boxed()
                .collect(groupingBy(c -> c, counting()))
                .values().stream()
                .filter(x -> x > 1).count();
    }
}
*/
public class CountingDuplicates {
    public static int duplicateCount(String text) {
        var t = text.toLowerCase();
        return (int) t.chars().filter(c -> t.indexOf(c) != t.lastIndexOf(c)).distinct().count();
    }
}
