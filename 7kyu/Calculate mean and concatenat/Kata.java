/*
You will be given an array which will include both integers and characters.

Return an array of length 2 with a[0] representing the mean of the ten integers
as a floating point number. There will always be 10 integers and 10 characters.
Create a single string with the characters and return it as a[1] while maintaining the original order.

lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']

Here is an example of your return

[3.6, "udiwstagwo"]

In C# and Java the mean return is a double.
*/

/*
import java.util.stream.IntStream;

import static java.lang.Character.*;
import static java.lang.Integer.*;
import static java.util.stream.Collectors.joining;

public class Kata {
    public static Object[] mean(char[] lst) {
        var mean = IntStream.range(0, lst.length)
                .filter(i -> isDigit(lst[i]))
                .map(i -> parseInt(String.valueOf(lst[i])))
                .summaryStatistics().getAverage();

        var chars = IntStream.range(0, lst.length)
                .distinct()
                .filter(i -> isLetter(lst[i]))
                .mapToObj(i -> String.valueOf(lst[i]))
                .collect(joining());

        return new Object[]{mean, chars};
    }
}*/

public class Kata {
    public static Object[] mean(char[] lst) {
        var str = new String(lst);
        return new Object[]{
                str.chars().filter(Character::isDigit).map(c -> c - '0').average().orElse(0),
                str.replaceAll("\\d", "")
        };
    }
}

/*
public class Kata {
    public static Object[] mean(char[] lst) {
        var sb = new StringBuilder();
        int sum = 0;
        for (char c : lst) {
            if (Character.isDigit(c))
                sum += c - '0';
            else sb.append(c);
        }
        return new Object[]{sum / 10.0, sb.toString()};
    }
}
*/
