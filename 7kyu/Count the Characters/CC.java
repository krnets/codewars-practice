/*
The goal of this kata is to write a function that takes two inputs:
a string and a character.
The function will count the number of times that character appears in the string.
The count is case insensitive.

For example:

        countChar("fizzbuzz","z") => 4
        countChar("Fancy fifth fly aloof","f") => 5

The character can be any alphanumeric character.
*/

/*
import java.util.HashMap;

public class CC {
    public static int charCount(String str, char c) {
        var counter = new HashMap<Character, Integer>();
        for (char s : str.toLowerCase().toCharArray()) {
            if (!counter.containsKey(s))
                counter.put(s, 1);
            else
                counter.put(s, counter.get(s) + 1);
        }
        return counter.getOrDefault(Character.toLowerCase(c), 0);
    }
}*/

/*
public class CC {
    public static int charCount(String str, char c) {
        return (int) str.toLowerCase().chars().filter(x -> x == Character.toLowerCase(c)).count();
    }
}
*/

public class CC {
    public static int charCount(String str, char c) {
        return (int) str.toLowerCase().chars().filter(x -> x == (c | 32)).count();
    }
}

/*
public class CC {
    public static int charCount(String str, char c) {
        int count = 0;
        for (char ch : str.toLowerCase().toCharArray())
            if (ch == Character.toLowerCase(c))
                count++;
        return count;
    }
}
*/
