/*
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet:
a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
*/

/*
import java.util.HashMap;

public class Kata {
    public static String high(String s) {
        int highest = 0;
        var scores = new HashMap<String, Integer>();

        for (String word : s.split(" ")) {
            int val = word.chars().map(ch -> ch - 'a' + 1).sum();
            scores.putIfAbsent(word, val);
            highest = Math.max(highest, val);
        }
        final int finalHighest = highest;

        return scores.entrySet().stream()
                .filter(e -> e.getValue() == finalHighest)
                .findFirst().get().getKey();
    }
}
*/

/*
import java.util.Arrays;
import java.util.Comparator;

public class Kata {
    public static String high(String s) {
        return Arrays.stream(s.split(" "))
                .max(Comparator.comparingInt(word -> word.chars()
                        .map(ch -> ch - 96)
                        .sum()))
                .orElse("");
    }
}
*/
/*
public class Kata {
    public static String high(String s) {
        return Arrays.stream(s.split(" "))
                .max(Comparator.comparingInt(word -> word.chars()
                        .map(ch -> ch - 96)
                        .sum()))
                .get();
    }
}
*/
public class Kata {
    public static String high(String s) {
        int start = 0, end = 0, prevWordStart, nextWordStart = 0, currWordScore = 0, highest = 0;

        for (int i = 0; i <= s.length(); i++) {
            char ch = (i == s.length() ? ' ' : s.charAt(i));
            if (ch != ' ')
                currWordScore += ch - 'a' + 1;
            else {
                prevWordStart = nextWordStart;
                nextWordStart = i + 1;
                if (currWordScore > highest) {
                    highest = currWordScore;
                    start = prevWordStart;
                    end = i;
                }
                currWordScore = 0;
            }
        }
        return s.substring(start, end);
    }
}
/*
public class Kata {
    public static String high(String s) {
        String winner = "";
        int highScore = 0;

        for (String word : s.split(" ")) {
            int score = 0;
            for (char c : word.toCharArray()) {
                score += c - 'a' + 1;
            }
            if (score > highScore) {
                winner = word;
                highScore = score;
            }
        }
        return winner;
    }
}*/
