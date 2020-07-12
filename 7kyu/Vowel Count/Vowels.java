/*
Return the number (count) of vowels in the given string.

        We will consider a, e, i, o, u as vowels for this Kata (but not y).

        The input string will only consist of lower case letters and/or spaces.
*/

/*
public class Vowels {
    public static int getCount(String str) {
        int vowelsCount = 0;
        for (int i = 0; i < str.length(); i++)
            if (String.valueOf(str.charAt(i)).matches("[aeiou]"))
                vowelsCount++;
        return vowelsCount;
    }
}*/
public class Vowels {
    public static int getCount(String str) {
        return str.replaceAll("(?i)[^aeou]", "").length();
    }
}
