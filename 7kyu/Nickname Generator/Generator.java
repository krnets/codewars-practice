/*If the string is less than 4 characters, return "Error: Name too short".

        Notes:

        Vowels are "aeiou", so discount the letter "y".
        Input will always be a string.
        Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
        The input can be modified
 */

/*
public class Generator {
    public static String nickname(String name) {
        return name.length() > 3 ? name.substring(0, name.matches("^.{2}[aeiou].+") ? 4 : 3) : "Error: Name too short";
    }
}
*/

public class Generator {
    public static String nickname(String name) {
        return name.length() > 3 ? name.substring(0, name.matches("^..[aeiou].+") ? 4 : 3) : "Error: Name too short";
    }
}
