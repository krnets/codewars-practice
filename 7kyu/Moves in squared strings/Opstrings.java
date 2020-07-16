/*
This kata is the first of a sequence of four about "Squared Strings".

        You are given a string of n lines, each substring being n characters long: For example:

        s = "abcd\nefgh\nijkl\nmnop"

        We will study some transformations of this square of strings.

        Vertical mirror: vert_mirror (or vertMirror or vert-mirror)

        vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"

        Horizontal mirror: hor_mirror (or horMirror or hor-mirror)

        hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"

        or printed:

        vertical mirror   |horizontal mirror
        abcd --> dcba     |abcd --> mnop
        efgh     hgfe     |efgh     ijkl
        ijkl     lkji     |ijkl     efgh
        mnop     ponm     |mnop     abcd

        Task:

        Write these two functions

        and

        high-order function oper(fct, s) where
        fct is the function of one variable f to apply to the string s (fct will be one of vertMirror, horMirror)

        Examples:

        s = "abcd\nefgh\nijkl\nmnop"
        oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
        oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"

        Note:

        The form of the parameter fct in oper changes according to the language. You can see each form according to the language in "Sample Tests".
        Bash Note:

        The input strings are separated by , instead of \n. The ouput strings should be separated by \r instead of \n. See "Sample Tests".

        Forthcoming katas will study other tranformations.
*/

/*

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Opstrings {
    public static String vertMirror(String strng) {
        return Stream.of(strng.split("\n")).map(s -> reverse(s)).collect(Collectors.joining("\n"));
    }

    private static String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }

    private static List<String> reverse(List<String> elements) {
        Collections.reverse(elements);
        return elements;
    }

    public static String horMirror(String strng) {
        return reverse(split(strng)).stream().collect(Collectors.joining("\n"));
    }

    private static List<String> split(String strng) {
        return Arrays.asList(strng.split("\n"));
    }

    public static String oper(Function<String, String> operator, String s) {
        return operator.apply(s);
    }
}*/

import java.util.Arrays;
import java.util.Collections;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Opstrings {
    public static String vertMirror(String strng) {
        return Stream.of(strng.split("\n"))
                .map(s -> new StringBuilder(s).reverse().toString())
                .collect(Collectors.joining("\n"));
    }
/*
    public static String horMirror(String strng) {
        var list = Arrays.asList(strng.split("\n"));
        Collections.reverse(list);
        return String.join("\n", list);
    }
*/

/*
    public static String horMirror(String strng) {
        var list = Arrays.asList(strng.split("\n"));
        Collections.reverse(list);
        return list.stream().collect(Collectors.joining("\n"));
    }
*/

    public static String horMirror(String strng) {
        return new StringBuilder(vertMirror(strng)).reverse().toString();
    }




    public static String oper(Function<String, String> operator, String s) {
        return operator.apply(s);
    }
}
