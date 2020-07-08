import java.util.Arrays;
import java.util.stream.Collectors;

/*
Define String.prototype.toAlternatingCase such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.

        StringUtils.toAlternativeString("hello world") == "HELLO WORLD"
        StringUtils.toAlternativeString("HELLO WORLD") == "hello world"
        StringUtils.toAlternativeString("hello WORLD") == "HELLO world"
        StringUtils.toAlternativeString("HeLLo WoRLD") == "hEllO wOrld"
        StringUtils.toAlternativeString("12345") == "12345" // Non-alphabetical characters are unaffected
        StringUtils.toAlternativeString("1a2b3c4d5e") == "1A2B3C4D5E"
        StringUtils.toAlternativeString("StringUtils.toAlternatingCase") == "sTRINGuTILS.TOaLTERNATINGcASE"

        As usual, your function/method should be pure, i.e. it should not mutate the original string.
*/
/*
public class StringUtils {
    public static String toAlternativeString(String string) {
        String result = "";
        for (int i = 0; i < string.length(); i++) {
            String c = string.substring(i, i + 1);
            if (c.toUpperCase().equals(c))
                result += c.toLowerCase();
            else
                result += c.toUpperCase();
        }
        return result;
    }
}*/
/*
public class StringUtils {
    public static String toAlternativeString(String string) {
        String result = "";
        for (char c : string.toCharArray()) {
            if (Character.isUpperCase(c))
                result += Character.toLowerCase(c);
            else result += Character.toUpperCase(c);
        }
        return result;
    }
}
*/
public class StringUtils {
    public static String toAlternativeString(String string) {
        return Arrays.stream(string.split(""))
                .map(c -> c.matches("[A-Z]") ? c.toLowerCase() : c.toUpperCase())
                .collect(Collectors.joining());
    }
}