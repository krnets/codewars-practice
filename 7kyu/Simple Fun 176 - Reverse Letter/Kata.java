/*
Given a string str, reverse it omitting all non-alphabetic characters.

        For str = "krishan", the output should be "nahsirk".
        For str = "ultr53o?n", the output should be "nortlu".

        [input] string str
        A string consists of lowercase latin letters, digits and symbols.

        [output] a string
*/

/*
public class Kata {
    public static String reverseLetter(final String str) {
        var result = new StringBuilder();
        for (int i = str.length() - 1; i > -1; i--)
            if (String.valueOf(str.charAt(i)).matches("[a-z]"))
                result.append(str.charAt(i));
        return result.toString();
    }
}*/
public class Kata {
    public static String reverseLetter(final String str) {
        return new StringBuilder(str.replaceAll("[^a-zA-Z]", "")).reverse().toString();
    }
}
