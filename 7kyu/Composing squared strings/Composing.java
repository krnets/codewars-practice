/*
A squared string is a string of n lines, each substring being n characters long.
We are given two n-squared strings. For example:

        s1 = "abcd\nefgh\nijkl\nmnop" s2 = "qrst\nuvwx\nyz12\n3456"

Let us build a new string strng of size (n + 1) x n in the following way:

The first line of strng has the first char of the first line of s1 plus the chars of the last line of s2.

The second line of strng has the first two chars of the second line of s1
plus the chars of the penultimate line of s2 except the last char

and so on until the nth line of strng has the n chars of the nth line of s1
plus the first char of the first line of s2.

Calling this function compose(s1, s2) we have:

        compose(s1, s2) -> "a3456\nefyz1\nijkuv\nmnopq"
        or printed:
        abcd    qrst  -->  a3456
        efgh    uvwx       efyz1
        ijkl    yz12       ijkuv
        mnop    3456       mnopq
*/

/*
public class Composing {
    public static String compose(String s1, String s2) {
        var res = new StringBuilder();
        var aa = s1.split("\n");
        var bb = s2.split("\n");
        for (int i = 0; i < aa.length; i++) {
            res.append(aa[i], 0, i + 1);
            res.append(bb[bb.length - i - 1], 0, bb.length - i);
            res.append("\n");
        }
        return res.toString().trim();
    }
}*/

import java.util.stream.*;

public class Composing {
    public static String compose(String s1, String s2) {
        var a = s1.split("\n");
        var b = s2.split("\n");
        return IntStream.range(0, a.length)
                .mapToObj(i -> a[i].substring(0, i + 1) + b[b.length - i - 1].substring(0, b.length - i))
                .collect(Collectors.joining("\n"));
    }
}
