/*
import java.util.HashMap;
import java.util.stream.Collectors;

abstract class Encoder {
    public abstract String encode(String source);
}

public class Leetspeak extends Encoder {
    static private final HashMap<String, String> dictionary = new HashMap<>();

    static {
        dictionary.put("a", "4");
        dictionary.put("e", "3");
        dictionary.put("l", "1");
        dictionary.put("m", "/^^\\");
        dictionary.put("o", "0");
        dictionary.put("u", "(_)");
    }

    @Override
    public String encode(String source) {
        return source == null ? "" : source.chars()
                .mapToObj(c -> dictionary.getOrDefault(
                        Character.toString(c).toLowerCase(), Character.toString(c)))
                .collect(Collectors.joining());
    }
}
*/

import java.util.Map;
import java.util.stream.Collectors;

abstract class Encoder {
    public abstract String encode(String source);
}

public class Leetspeak extends Encoder {
    static Map<Character, Object> dictionary = Map.of('a', 4, 'e', 3, 'l', 1, 'm', "/^^\\", 'o', 0, 'u', "(_)");

    @Override
    public String encode(String source) {
        return source == null ? "" : source.chars()
                .mapToObj(c -> String.valueOf(dictionary.getOrDefault(Character.toLowerCase((char) c), Character.toString(c))))
                .collect(Collectors.joining());
    }
}
