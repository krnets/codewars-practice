import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class MorseCodeDecoder {
    private static final int CHAR_PAUSE = 3;
    private static final int WORD_PAUSE = 7;

    public static String decodeBits(String bits) {
        String bitsTrimmed = bits.replaceAll("^0+|0+$", "");
        int transmissionRate = Pattern.compile("0+|1+").matcher(bitsTrimmed).results()
                .mapToInt(m -> m.group(0).length())
                .min().orElse(1);

        String[] words = bitsTrimmed.split("0".repeat(WORD_PAUSE * transmissionRate));
        var sb = new StringBuilder();

        for (String word : words) {
            var letters = word.split("0".repeat(CHAR_PAUSE * transmissionRate));

            for (String letter : letters) {
                var dots = letter.split("0".repeat(transmissionRate));

                for (String dot : dots)
                    if (dot.length() > transmissionRate) {
                        sb.append("-");
                    } else {
                        sb.append(".");
                    }
                sb.append(" ");
            }
            sb.append("  ");
        }
        return sb.toString();
    }

    public static String decodeMorse(String morseCode) {
        return Arrays.stream(morseCode.split("\\s{" + CHAR_PAUSE + "}"))
                .map(word -> Arrays.stream(word.split(" "))
                        .map(MorseCode::get)
                        .collect(Collectors.joining()))
                .collect(Collectors.joining(" "));
    }
}
