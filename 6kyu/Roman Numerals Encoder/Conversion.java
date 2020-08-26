/*
Create a function taking a positive integer as its parameter and returning a string
containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with
the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.

2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.


        conversion.solution(1000); //should return "M"


        Symbol    Value
        I          1
        V          5
        X          10
        L          50
        C          100
        D          500
        M          1,000

Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
 */

/*
public class Conversion {
    public String solution(int n) {
        var romanSymbols = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        var romanSymbolVals = new Integer[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        var output = new StringBuilder();
        for (int i = 0; i < romanSymbolVals.length; i++) {
            int val = romanSymbolVals[i];
            while (n - val >= 0) {
                output.append(romanSymbols[i]);
                n -= val;
            }
        }
        return output.toString();
    }
}
*/

/*
public class Conversion {
    private final String[] romanSymbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    private final Integer[] romanVals = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    public String solution(int n) {
        var sb = new StringBuilder();
        for (int i = 0; i < romanVals.length; i++) {
            int val = romanVals[i];
            while (n - val >= 0) {
                sb.append(romanSymbols[i]);
                n -= val;
            }
        }
        return sb.toString();
    }
}
*/

import java.util.Collections;
import java.util.TreeMap;

public class Conversion {
    private final static TreeMap<Integer, String> romanNum = new TreeMap<>(Collections.reverseOrder());

    static {
        romanNum.put(1, "I");
        romanNum.put(4, "IV");
        romanNum.put(5, "V");
        romanNum.put(9, "IX");
        romanNum.put(10, "X");
        romanNum.put(40, "XL");
        romanNum.put(50, "L");
        romanNum.put(90, "XC");
        romanNum.put(100, "C");
        romanNum.put(400, "CD");
        romanNum.put(500, "D");
        romanNum.put(900, "CM");
        romanNum.put(1000, "M");
    }

    public String solution(int n) {
        var sb = new StringBuilder();
        for (var e : romanNum.entrySet()) {
            var i = e.getKey();
            var roman = e.getValue();
            while (n >= i) {
                sb.append(roman);
                n -= i;
            }
        }
        return sb.toString();
    }
}

/*
public class Conversion {
    private final static TreeMap<Integer, String> romanNum = new TreeMap<>();

    static {
        romanNum.put(1000, "M");
        romanNum.put(900, "CM");
        romanNum.put(500, "D");
        romanNum.put(400, "CD");
        romanNum.put(100, "C");
        romanNum.put(90, "XC");
        romanNum.put(50, "L");
        romanNum.put(40, "XL");
        romanNum.put(10, "X");
        romanNum.put(9, "IX");
        romanNum.put(5, "V");
        romanNum.put(4, "IV");
        romanNum.put(1, "I");
    }

    public String solution(int n) {
        Integer key = romanNum.floorKey(n);

        if (n == key)
            return romanNum.get(key);

        return romanNum.get(key) + solution(n - key);
    }
}*/
