/*
You are going to be given a string.
Your job is to return that string in a certain order that I will explain below:

        Let's say you start with this: 012345

        The first thing you do is reverse it:543210
        Then you will take the string from the 1st position and reverse it again:501234
        Then you will take the string from the 2nd position and reverse it again:504321
        Then you will take the string from the 3rd position and reverse it again:504123

        Continue this pattern until you have done every single position,
        and then you will return the string you have created.
        For this particular number, you would return:504132

        #Input: A string of length 1 - 1000

        #Output: A correctly reordered string.
*/

/*
import java.util.ArrayList;

public class FunReverse {
    public static String funReverse(String s) {
        var strings = new ArrayList<String>();
        strings.add(s);
        for (int i = 0; i < s.length() - 1; i++) {
            var last = strings.get(strings.size() - 1);
            strings.add(last.substring(0, i) + new StringBuilder(last.substring(i)).reverse());
        }
        return strings.get(strings.size() - 1);
    }
}
*/

/*
public class FunReverse {
    public static String funReverse(String s) {
        if (s.length() == 1)
            return s;
        return s.charAt(s.length() - 1) + funReverse(new StringBuilder(s).reverse().substring(1));
    }
}*/

public class FunReverse {
    public static String funReverse(String s) {
        for (int i = 0; i < s.length(); i += 2) {
            s = s.substring(0, i) + s.substring(s.length() - 1) + s.substring(i, s.length() - 1);
        }
        return s;
    }
}
