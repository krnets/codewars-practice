import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class TopWords {

    public static List<String> top3(String s) {
        Pattern regex = Pattern.compile("([a-z]+'?[a-z']*)");

        Map<String, Long> map = regex
                .matcher(s.toLowerCase())
                .results()
                .map(m -> m.group(1))
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        return map.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .limit(3)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
    }
}
