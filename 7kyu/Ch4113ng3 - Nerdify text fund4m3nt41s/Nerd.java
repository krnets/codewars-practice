/*
Make your strings more nerdy:
Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1
e.g. "Fundamentals" --> "Fund4m3nt41s"
*/

/*
import java.util.Map;
import java.util.stream.Collectors;

class Nerd {
    private static Map<String, String> trans = Map.of("a", "4", "A", "4", "e", "3", "E", "3", "l", "1");

    public static String nerdify(String txt) {
        return txt.chars()
                .mapToObj(c -> trans.getOrDefault("" + (char) c, "" + (char) c))
                .collect(Collectors.joining());
    }
}*/

class Nerd {
    public static String nerdify(String txt) {
        return txt.replaceAll("[aA]", "4").replaceAll("[eE]", "3").replaceAll("l", "1");
    }
}
