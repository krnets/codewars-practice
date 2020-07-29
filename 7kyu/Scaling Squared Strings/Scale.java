/*
You are given a string of n lines, each substring being n characters long. For example:

        s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
        A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
        Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

Example: a = "abcd\nefgh\nijkl\nmnop"
        scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"

        Printed:

        abcd   ----->   aabbccdd
        efgh            aabbccdd
        ijkl            aabbccdd
        mnop            eeffgghh
        eeffgghh
        eeffgghh
        iijjkkll
        iijjkkll
        iijjkkll
        mmnnoopp
        mmnnoopp
        mmnnoopp

Task :  Write function scale(strng, k, v) k and v will be positive integers. If strng == "" return "".
*/


/*
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Scale {
    public static String scale(String strng, int k, int v) {
        if (strng.isEmpty()) return strng;

        var list = new ArrayList<String>();

        for (String s : strng.split("\n"))
            for (int i = 0; i < v; i++)
                list.add(Arrays.stream(s.split(""))
                        .map(c -> c.repeat(k))
                        .collect(Collectors.joining()));

        return String.join("\n", list);
    }
}*/

import static java.util.Collections.nCopies;

public class Scale {
    public static String scale(String strng, int k, int v) {
        return strng.replaceAll("(.)",  String.join("",   nCopies(k, "$1")))
                    .replaceAll("(.+)", String.join("\n", nCopies(v, "$1")));
    }
}

