public class Kata {

    public static String intToNegabinary(int i) {
        var sb = new StringBuilder();

        while (i != 0) {
            int remainder = Math.abs(i) % 2;
            sb.append(remainder);
            if (i < 0 && remainder > 0) i--;
            i /= -2;
        }
        var result = sb.reverse().toString();
        return result.isEmpty() ? "0" : result;
    }

    public static int negabinaryToInt(String s) {
        var strReversed = new StringBuilder(s).reverse();
        int result = 0;

        for (int i = 0; i < strReversed.length(); i++)
            if (strReversed.charAt(i) == '1')
                result += Math.pow(-2, i);

        return result;
    }
}
