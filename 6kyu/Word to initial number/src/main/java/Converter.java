import java.util.HashMap;

public class Converter {
    public static long convert(String word) {
        var map = new HashMap<Character, Integer>();
        var sb = new StringBuilder();
        int count = 0;

        for (char c : word.toLowerCase().toCharArray()) {
            if (!map.containsKey(c)) {
                map.put(c, count > 1 ? count : 1 - count);
                count++;
            }
            sb.append(map.get(c));
        }
        return sb.length() > 0 ? Long.parseLong(sb.toString()) : 0;
    }
}