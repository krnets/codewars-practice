/*
You need to write a function, that returns the first non-repeated character in the given string.

For example for string "test" function should return 'e'. For string "teeter" function should return 'r'.

If a string contains all unique characters, then return just the first character of the string.

Example: for input "trend" function should return 't'

You can assume, that the input string has always non-zero length.

If there is no repeating character, return null
*/

import java.util.HashMap;
import java.util.LinkedHashMap;

import static java.util.stream.Collectors.*;

/*
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        var counter = new HashMap<Character, Integer>();
        for (int i = 0; i < source.length(); i++) {
            char c = source.charAt(i);
            if (!counter.containsKey(c)) counter.put(c, 1);
            else counter.put(c, counter.get(c) + 1);
        }
        for (int i = 0; i < source.length(); i++) {
            char c = source.charAt(i);
            if (counter.get(c) == 1) return c;
        }
        return null;
    }
}*/
/*
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        var counter = new HashMap<Character, Integer>();
        for (char c : source.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }
        for (char c : source.toCharArray()) {
            if (counter.get(c) == 1)
                return c;
        }
        return null;
    }
}
*/
/*
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        for (int i = 0; i < source.length(); i++) {
            char c = source.charAt(i);
            if (source.indexOf(c) == source.lastIndexOf(c))
                return c;
        }
        return null;
    }
}
*/
/*
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        for (char c : source.toCharArray()) {
            if (source.indexOf(c) == source.lastIndexOf(c))
                return c;
        }
        return null;
    }
}
*/

/*
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        return source.chars()
                .mapToObj(c -> (char) c)
                .collect(groupingBy(c -> c, LinkedHashMap::new, counting()))
                .entrySet().stream()
                .filter(e -> e.getValue() == 1)
                .map(e -> e.getKey())
                .findFirst().orElse(null);
    }
}
*/

/*
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        return source.codePoints()
                .filter(c -> source.indexOf(c) == source.lastIndexOf(c))
                .mapToObj(c -> (char) c)
                .findFirst().orElse(null);
    }
}
*/
public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        return source.chars()
                .filter(c -> source.indexOf(c) == source.lastIndexOf(c))
                .mapToObj(c -> (char) c)
                .findFirst().orElse(null);
    }
}
