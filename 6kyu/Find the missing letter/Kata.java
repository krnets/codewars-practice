/*
Write a method that takes an array of consecutive (increasing) letters
as input and that returns the missing letter in the array.

You will always get an valid array.
And it will be always exactly one letter be missing.
The length of the array will always be at least 2.
The array will always contain letters in only one case.

        ['a','b','c','d','f'] -> 'e'
        ['O','Q','R','S'] -> 'P'

(Use the English alphabet with 26 letters!)
*/

/*
import java.util.ArrayList;

public class Kata {
    public static char findMissingLetter(char[] array) {
        var list = new ArrayList<Character>();

        for (char c : array)
            list.add(c);

        for (int i = array[0]; i < array[array.length - 1]; i++) {
            var x = (char) i;
            if (!list.contains(x))
                return x;
        }
        return array[0];
    }
}*/

public class Kata {
    public static char findMissingLetter(char[] array) {
        var expected = array[0];
        for (char c : array) {
            if (c != expected) break;
            expected++;
        }
        return expected;
    }
}

/*
import java.util.stream.IntStream;

public class Kata {
    public static char findMissingLetter(char[] array) {
        int index = IntStream.range(0, array.length - 1)
                .filter(i -> array[i] != array[i + 1] - 1)
                .findFirst()
                .getAsInt();

        return (char) (array[index] + 1);
    }
}
*/
