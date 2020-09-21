/*
Your task is to find the next higher number (int) with same '1'- Bits.

I.e. as much 1 bits as before and output next higher than input.
Input is always an int in between 1 and 1<<30 (inclusive).
No bad cases or special tricks...

Some easy examples:

        Input: 129  => Output: 130 (10000001 => 10000010)
        Input: 127 => Output: 191 (01111111 => 10111111)
        Input: 1 => Output: 2 (01 => 10)
        Input: 323423 => Output: 323439 (1001110111101011111 => 1001110111101101111)
*/

/*
import java.util.function.Function;

public class Kata {
    public static int nextHigher(int n) {
        Function<Integer, Integer> calcBits = x -> Integer.toBinaryString(x).replace("0", "").length();
        Integer nBits = calcBits.apply(n);
        int nextVal = n + 1;

        while (!calcBits.apply(nextVal).equals(nBits))
            nextVal++;

        return nextVal;
    }
}
*/

public class Kata {
    public static int nextHigher(int n) {
        int nBits = Integer.bitCount(n);
        int nextVal = n + 1;

        while (Integer.bitCount(nextVal) != nBits)
            nextVal++;

        return nextVal;
    }
}

/*
import java.util.stream.IntStream;

public class Kata {
    public static int nextHigher(int n) {
        int nBits = Integer.bitCount(n);

        return IntStream.iterate(n + 1, i -> i + 1)
                .filter(i -> Integer.bitCount(i) == nBits)
                .findFirst().orElse(0);
    }
}
*/
