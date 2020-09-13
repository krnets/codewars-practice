/*
Everyone knows passphrases. One can choose passphrases from poems, songs, movies names
and so on but frequently they can be guessed due to common cultural references.
You can get your passphrases stronger by different means.
One is the following:

Choose a text in capital letters including or not digits and non alphabetic characters,
shift each letter by a given number but the transformed letter must be a letter (circular shift),
replace each digit by its complement to 9,
keep such as non alphabetic and non digit characters,
down-case each letter in odd position, up-case each letter in even position
(the first character is in position 0),
reverse the whole result.

Example:
        your text: "BORN IN 2015!", shift 1

        1 + 2 + 3 -> "CPSO JO 7984!"

        4 "CpSo jO 7984!"

        5 "!4897 Oj oSpC"

        With longer passphrases it's better to have a small and easy program.
        https://en.wikipedia.org/wiki/Passphrase
*/

public class PlayPass {
    public static String playPass(String s, int n) {
        var sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c))
                sb.append(Math.abs(Character.getNumericValue(c) - 9));

            else if (Character.isLetter(c)) {
                var shifted = (char) ((c + n - 'A') % 26 + 'A');

                if (i % 2 == 0) {
                    sb.append(Character.toUpperCase(shifted));
                } else {
                    sb.append(Character.toLowerCase(shifted));
                }

            } else
                sb.append(c);
        }
        return sb.reverse().toString();
    }
}

