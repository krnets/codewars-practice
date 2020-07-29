/*
Given a string S.
You have to return another string such that even-indexed and odd-indexed characters of S
are grouped and groups are space-separated (see sample below)

Note:   0 is considered to be an even index.
        All input strings are valid with no spaces

        input: 'CodeWars'
        output 'CdWr oeas'

        S[0] = 'C'
        S[1] = 'o'
        S[2] = 'd'
        S[3] = 'e'
        S[4] = 'W'
        S[5] = 'a'
        S[6] = 'r'
        S[7] = 's'

        Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
        odd ones are 1, 3, 5, 7, so the second group is 'oeas'
        And the final string to return is 'Cdwr oeas'
*/

/*
public class OddEvenSort {
    public static String sortMyString(String s) {
        var even = new StringBuilder();
        var odd = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0) even.append(s.charAt(i));
            else odd.append(s.charAt(i));
        }
        return even + " " + odd;
    }
}*/

/*
public class OddEvenSort {
    public static String sortMyString(String s) {
        var even = new StringBuilder();
        var odd = new StringBuilder();
        boolean toggle = false;
        for (char c : s.toCharArray()) {
            if (toggle = !toggle) even.append(c);
            else odd.append(c);
        }
        return String.format("%s %s", even.toString(), odd.toString());
    }
}
*/
/*
public class OddEvenSort {
    public static String sortMyString(String s) {
        var even = new StringBuilder();
        var odd = new StringBuilder();
        boolean toggle = false;
        for (char c : s.toCharArray()) {
            if (toggle = !toggle) even.append(c);
            else odd.append(c);
        }
        return even + " " + odd;
    }
}
*/

public class OddEvenSort {
    public static String sortMyString(String s) {
        return s.replaceAll("(.).", "$1") + " " + s.replaceAll(".(.)?", "$1");
    }
}
