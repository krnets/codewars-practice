/*
public class Primitive {

    public String determineType(String number) {
        try {
            long n = Long.parseLong(number);
            if (n >= Byte.MIN_VALUE && n <= Byte.MAX_VALUE) return "byte";
            if (n >= Short.MIN_VALUE && n <= Short.MAX_VALUE) return "short";
            if (n >= Integer.MIN_VALUE && n <= Integer.MAX_VALUE) return "int";
            return "long";
        } catch (NumberFormatException e) {
            return "none";
        }
    }
}*/

import java.math.BigInteger;

public class Primitive {

    public String determineType(String number) {
        int bitLength = new BigInteger(number).bitLength();

        if (bitLength < 8) return "byte";
        if (bitLength < 16) return "short";
        if (bitLength < 32) return "int";
        if (bitLength < 64) return "long";
        return "none";
    }
}
