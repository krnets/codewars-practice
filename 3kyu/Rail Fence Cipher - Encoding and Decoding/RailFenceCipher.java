public class RailFenceCipher {

    static String encode(String s, int n) {
        return railTranspose(s, n, true);
    }

    static String decode(String s, int n) {
        return railTranspose(s, n, false);
    }

    private static String railTranspose(String data, int rails, boolean encrypt) {
        var transposedChars = new char[data.length()];

        for (int k = 0, pos = 0; k < rails; k++) {
            int index = k;
            boolean down = true;

            while (index < data.length()) {
                if (encrypt) transposedChars[pos++] = data.charAt(index);
                else         transposedChars[index] = data.charAt(pos++);

                if (k == 0 || k == rails - 1) {
                    index = index + 2 * (rails - 1);
                } else if (down) {
                    index = index + 2 * (rails - k - 1);
                    down = false;
                } else {
                    index = index + 2 * k;
                    down = true;
                }
            }
        }

        return new String(transposedChars);
    }
}