/*
import org.apache.commons.text.similarity.LevenshteinDistance;

import java.util.Arrays;
import java.util.Comparator;

public class Dictionary {

    private final String[] words;
    private final int maxWordLength;

    public Dictionary(String[] words) {
        this.words = words;
        maxWordLength = Arrays.stream(words).max(Comparator.comparingInt(String::length)).get().length();
    }

    public String findMostSimilar(String to) {
        int check = 0;
        String result = "";
        LevenshteinDistance ld = LevenshteinDistance.getDefaultInstance();

        for (String word : words) {
            int gdl = ld.apply(to, word);

            if ((maxWordLength - gdl) > check) {
                check = (maxWordLength - gdl);
                result = word;
            }
        }
        return result;
    }
}
*/

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class Dictionary {

    private final String[] words;

    public Dictionary(String[] words) {
        this.words = words;
    }

    public String findMostSimilar(String to) {
        return Arrays.stream(words)
                .min(Comparator.comparingInt(word -> getSimilarPoints(word, to)))
                .get();
    }

    private int getSimilarPoints(String word, String to) {
        return Math.max(word.length(), to.length()) - similarLetters(word, to);
    }

    private int similarLetters(String word, String to) {
        if (word.length() > to.length()) {
            return similarLetters(to, word);
        }
        return IntStream.rangeClosed(0, to.length() - word.length())
                .map(i -> (int) IntStream.range(0, word.length())
                        .filter(j -> word.charAt(j) == to.charAt(i + j)).count())
                .max().orElse(0);
    }
}
