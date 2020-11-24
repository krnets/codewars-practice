/*
import java.text.DecimalFormat;
import java.util.concurrent.atomic.AtomicReference;
import java.util.regex.Pattern;

public class Trumpdetector {
    public static double detect(String trumpySpeech) {
        var vowelsOnly = Pattern.compile("[a]+|[e]+|[i]+|[o]+|[u]+");
        var countTotalVowels = new AtomicReference<>(0.0);
        var countExtraVowels = new AtomicReference<>(0.0);

        vowelsOnly.matcher(trumpySpeech.toLowerCase()).results()
                .forEach(m -> {
                    countTotalVowels.getAndSet(countTotalVowels.get() + 1);
                    countExtraVowels.updateAndGet(v -> v + m.group(0).length() - 1);
                });

        var ratio = countExtraVowels.get() / countTotalVowels.get();
        var df = new DecimalFormat("#.##");
        return Double.parseDouble(df.format(ratio));
    }
}*/

/*
import java.text.DecimalFormat;
import java.util.regex.Pattern;

public class Trumpdetector {
    public static double detect(String trumpySpeech) {
        var pattern = Pattern.compile("([aeiou])(\\1*)", Pattern.CASE_INSENSITIVE);
        var matcher = pattern.matcher(trumpySpeech);
        double countTotalVowels = 0.0;
        double countExtraVowels = 0.0;

        while (matcher.find()) {
            countTotalVowels++;
            countExtraVowels += matcher.group(0).length() - 1;
        }
        var ratio = countExtraVowels / countTotalVowels;
        var df = new DecimalFormat("#.##");
        return Double.parseDouble(df.format(ratio));
    }
}
*/

import java.text.DecimalFormat;
import java.util.regex.Pattern;

public class Trumpdetector {
    public static double detect(String trumpySpeech) {
        var pattern = Pattern.compile("([aeiou])(\\1*)", Pattern.CASE_INSENSITIVE);
        var matcher = pattern.matcher(trumpySpeech);
        int countTotalVowels = 0;
        int countExtraVowels = 0;

        while (matcher.find()) {
            countTotalVowels++;
            countExtraVowels += matcher.group(0).length() - 1;
        }
        var ratio = (double) countExtraVowels / countTotalVowels;
        var df = new DecimalFormat("#.##");
        return Double.parseDouble(df.format(ratio));
    }
}
