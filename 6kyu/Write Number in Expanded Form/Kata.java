/*
You will be given a number and you will need to return it as a string in Expanded Form. For example:

        Kata.expandedForm(12); # Should return "10 + 2"
        Kata.expandedForm(42); # Should return "40 + 2"
        Kata.expandedForm(70304); # Should return "70000 + 300 + 4"

NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
*/

import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
public class Kata {
    public static String expandedForm(int num) {
        return IntStream.range(0, (num + "").length())
                .mapToObj(i -> (num + "").charAt(i) + "0".repeat((num + "").length() - 1 - i))
                .filter(c -> !c.matches("0+"))
                .collect(Collectors.joining(" + "));
    }
}
*/
/*
public class Kata {
    public static String expandedForm(int num) {
        String strNum = String.valueOf(num);

        return IntStream.range(0, strNum.length())
                .mapToObj(i -> ((strNum.charAt(i) - '0') * (int) Math.pow(10, strNum.substring(i).length() - 1)) + "")
                .filter(c -> !c.equals("0"))
                .collect(Collectors.joining(" + "));
    }
}
*/

/*
public class Kata {
    public static String expandedForm(int num) {
        var sb = new StringBuilder();
        int multiplier = 1;
        while (num > 0) {
            int nextDigit = num % 10;
            num /= 10;
            if (nextDigit > 0) {
                sb.insert(0, multiplier * nextDigit);
                sb.insert(0, " + ");
            }
            multiplier *= 10;
        }
        return sb.substring(3);
    }
}
*/
import java.util.LinkedList;

public class Kata {
    public static String expandedForm(int num) {
        var list = new LinkedList<String>();
        for (int d, m = 1; num > 0; m *= 10) {
            d = (num % 10) * m;
            if (d > 0)
                list.push(String.valueOf(d));
            num /= 10;
        }
        return String.join(" + ", list);
    }
}
