/*
Write a function

        TripleDouble(long num1, long num2)

which takes numbers num1 and num2
and returns 1 if there is a straight triple of a number at any place in num1
and also a straight double of the same number in num2.

If this isn't the case, return 0

        TripleDouble(451999277, 41177722899) == 1
        // num1 has straight triple 999s and
        // num2 has straight double 99s

        TripleDouble(1222345, 12345) == 0
        // num1 has straight triple 2s but num2 has only a single 2

        TripleDouble(12345, 12345) == 0

        TripleDouble(666789, 12345667) == 1
*/

/*
import static java.lang.String.valueOf;

public class Kata {
    public static int TripleDouble(long num1, long num2) {
        for (int i = 0; i < 10; i++) {
            var x = valueOf(i);
            var xTriple = x.repeat(3);
            var xDouble = x.repeat(2);

            if (valueOf(num1).contains(xTriple) && valueOf(num2).contains(xDouble))
                return 1;
        }
        return 0;
    }
}
*/

public class Kata {
    public static int TripleDouble(long num1, long num2) {
        var num1str = String.valueOf(num1);
        var num2str = String.valueOf(num2);

        for (int i = 0; i < 10; i++) {
            var x = String.valueOf(i);
            var xTriple = x.repeat(3);
            var xDouble = x.repeat(2);

            if (num1str.contains(xTriple) && num2str.contains(xDouble))
                return 1;
        }
        return 0;
    }
}
/*
public class Kata {
    public static int TripleDouble(long num1, long num2) {
        var num1str = String.valueOf(num1);
        var num2str = String.valueOf(num2);

        for (int i = 0; i < 10; i++)
            if (isRepeating(num1str, i, 3) && isRepeating(num2str, i, 2))
                return 1;

        return 0;
    }

    private static boolean isRepeating(String s, int value, int nRepeats) {
        return s.matches(".*(" + value + ")" + "{" + nRepeats + "}.*");
    }
}
*/
