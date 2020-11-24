public class Kata {

    public static String encrypt(final String text, final int n) {
        return processText(text, n, true);
    }

    public static String decrypt(final String encryptedText, final int n) {
        return processText(encryptedText, n, false);
    }

    private static String processText(String str, int n, boolean encrypt) {
        while (n-- > 0) {
            var sb = new StringBuilder();
            int end = encrypt ? str.length() - 1 : str.length() / 2;
            int step = encrypt ? 2 : 1;

            for (int i = 0; i < end; i += step) {
                if (encrypt) sb.insert(i / 2, str.charAt(i + 1));
                else sb.append(str.charAt(i + end));
                sb.append(str.charAt(i));
            }
            if (str.length() % 2 == 1)
                sb.append(str.charAt(str.length() - 1));

            str = sb.toString();
        }
        return str;
    }
}