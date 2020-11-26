import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Parser {

    static HashMap<String, Integer> map = new HashMap<>();

    static {
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        map.put("four", 4);
        map.put("five", 5);
        map.put("six", 6);
        map.put("seven", 7);
        map.put("eight", 8);
        map.put("nine", 9);
        map.put("ten", 10);
        map.put("eleven", 11);
        map.put("twelve", 12);
        map.put("thirteen", 13);
        map.put("fourteen", 14);
        map.put("fifteen", 15);
        map.put("sixteen", 16);
        map.put("seventeen", 17);
        map.put("eighteen", 18);
        map.put("nineteen", 19);
        map.put("twenty", 20);
        map.put("thirty", 30);
        map.put("forty", 40);
        map.put("fifty", 50);
        map.put("sixty", 60);
        map.put("seventy", 70);
        map.put("eighty", 80);
        map.put("ninety", 90);
        map.put("hundred", 100);
        map.put("thousand", 1_000);
        map.put("million", 1_000_000);
    }

    static List<String> ordersMagnitude = List.of("hundred", "thousand", "million");

    public static int parseInt(String numStr) {
        numStr = numStr.replaceAll("( and)|-", " ");
        String[] words = numStr.split("\\s+");
        ArrayList<List<String>> sections = new ArrayList<>();
        ArrayList<Integer> values = new ArrayList<>();
        int indexThousand = 0;

        for (int i = 0; i < words.length; i++) {
            if (words[i].equals("thousand")) {
                String[] slice = Arrays.copyOfRange(words, indexThousand, i + 1);
                List<String> section = Arrays.asList(slice);
                sections.add(section);
                indexThousand = i + 1;
            } else if (i == words.length - 1) {
                String[] slice = Arrays.copyOfRange(words, indexThousand, i + 1);
                List<String> section = Arrays.asList(slice);
                sections.add(section);
            }
        }

        for (List<String> section : sections) {
            int sectionResult = 0;

            for (String word : section) {
                int value = map.getOrDefault(word, 0);

                if (ordersMagnitude.contains(word)) {
                    sectionResult *= value;
                } else {
                    sectionResult += value;
                }
            }
            values.add(sectionResult);
        }
        return values.stream().reduce(0, Integer::sum);
    }
}