/*
import java.util.stream.Collectors;

class Crypto {
    public static String wordPattern(final String word) {
        String distinctChars = word.toLowerCase()
                .chars()
                .distinct()
                .mapToObj(Character::toString)
                .collect(Collectors.joining());

        return word.toLowerCase()
                .chars()
                .mapToObj(distinctChars::indexOf)
                .map(String::valueOf)
                .collect(Collectors.joining("."));
    }
}*/

import java.util.HashMap;
import java.util.Map;

class Crypto {
    public static String wordPattern(final String word) {
        Map<Integer, Integer> lettersMap = new HashMap<>();

        String[] arr = word.toLowerCase().chars()
                .mapToObj(c -> String.valueOf(lettersMap.computeIfAbsent(c, k -> lettersMap.size())))
                .toArray(String[]::new);

        return String.join(".", arr);
    }
}