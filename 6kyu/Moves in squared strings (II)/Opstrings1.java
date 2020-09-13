/*
You are given a string of n lines, each substring being n characters long:
For example:

        s = "abcd\nefgh\nijkl\nmnop"

        We will study some transformations of this square of strings.

        Clock rotation 180 degrees: rot

        rot(s) => "ponm\nlkji\nhgfe\ndcba"

        selfieAndRot
        It is initial string + string obtained by clock rotation 180 degrees
        with dots interspersed in order (hopefully) to better show the rotation when printed.

        s = "abcd\nefgh\nijkl\nmnop" -->
        "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"

        or printed:

        |rotation        |selfie_and_rot
        |abcd --> ponm   |abcd --> abcd....
        |efgh     lkji   |efgh     efgh....
        |ijkl     hgfe   |ijkl     ijkl....
        |mnop     dcba   |mnop     mnop....
        ....ponm
        ....lkji
        ....hgfe
        ....dcba

Task:

        Write these two functions rotand selfie_and_rot

        and

        high-order function oper(fct, s) where
        fct is the function of one variable f to apply to the string s
        (fct will be one of rot, selfie_and_rot)

Examples:

        s = "abcd\nefgh\nijkl\nmnop"

        oper(rot, s) => "ponm\nlkji\nhgfe\ndcba"

        oper(selfie_and_rot, s) =>
        "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"

Notes:

        The form of the parameter fct in oper changes according to the language.
        You can see each form according to the language in "Your test cases".
        It could be easier to take these katas from number (I) to number (IV)
*/

import java.util.function.UnaryOperator;

class Opstrings1 {

    public static String rot(String strng) {
        return new StringBuilder(strng).reverse().toString();
    }

    public static String selfieAndRot(String strng) {
        String dots = ".".repeat(strng.indexOf("\n"));
        String mid = dots + "\n" + dots;
        String rotated = rot(strng).replace("\n", "\n" + dots);

        return strng.replace("\n", dots + "\n") + mid + rotated;
    }

    public static String oper(UnaryOperator<String> operator, String s) {
        return operator.apply(s);
    }
}