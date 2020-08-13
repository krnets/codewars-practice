/*
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).


        toCamelCase("the-stealth-warrior"); // returns "theStealthWarrior"
        toCamelCase("The_Stealth_Warrior"); // returns "TheStealthWarrior"
*/

/*
public class Solution {
    static String toCamelCase(String s) {
        var arr = s.split(s.contains("-") ? "-" : "_");
        for (int i = 1; i < arr.length; i++) {
            arr[i] = arr[i].substring(0, 1).toUpperCase() + arr[i].substring(1);
        }
        return String.join("", arr);
    }
}
*/
/*
public class Solution {
    static String toCamelCase(String s) {
        var arr = s.split("[-_]");
        for (int i = 1; i < arr.length; i++) {
            arr[i] = arr[i].substring(0, 1).toUpperCase() + arr[i].substring(1);
        }
        return String.join("", arr);
    }
}
*/

/*
import java.util.Arrays;
import java.util.stream.Collectors;

public class Solution {
    static String toCamelCase(String s) {
        var arr = s.split("[-_]");
        return arr[0] + Arrays.stream(arr).skip(1)
                .map(x -> x.substring(0, 1).toUpperCase() + x.substring(1))
                .collect(Collectors.joining());
    }
}
*/

import java.util.regex.Pattern;

public class Solution {
    static String toCamelCase(String s) {
        return Pattern.compile("[-|_]+(\\w)").matcher(s).replaceAll(m -> m.group(1).toUpperCase());
    }
}