/*
Write a function that takes an integer as input, and returns the number of bits
that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case
*/

/*
public class BitCounting {
    public static int countBits(int n) {
        return Integer.bitCount(n);
    }
}*/


/*
public class BitCounting {
    public static int countBits(int n) {
        int bits = 0, bitShift = 1;
        while (bitShift <= n) {
            if (bitShift == (n & bitShift))
                bits++;
            bitShift <<= 1;
        }
        return bits;
    }
}
*/

public class BitCounting {
    public static int countBits(int n) {
        int bits = 0;
        while (n > 0) {
            bits += n & 1;
            n >>= 1;
        }
        return bits;
    }
}
/*
public class BitCounting {
    public static int countBits(int n) {
        return (int) Integer.toBinaryString(n).chars()
                .filter(c -> c == '1')
                .count();
    }
}
*/

/*
public class BitCounting {
    public static int countBits(int n) {
        var binary = Integer.toBinaryString(n);
        return binary.length() - binary.replace("1", "").length();
    }
}
*/

/*
public class BitCounting {
    public static int countBits(int n) {
        int bits = 0;
        do bits += n % 2; while ((n /= 2) > 0);
        return bits;
    }
}
*/

/*
public class BitCounting {
    public static int countBits(int n) {
        return n == 0 ? 0 : (n & 1) + countBits(n >>> 1);
    }
}
*/
