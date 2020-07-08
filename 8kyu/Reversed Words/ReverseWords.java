/*
public class ReverseWords {
    public static String reverseWords(String str) {
        String[] words = str.split(" ");
        String[] arr = new String[words.length];
        for (int i = 0; i < words.length; i++) {
            arr[words.length - i - 1] = words[i];
        }
        String result = "";
        for (String word : arr) {
            result += word;
            result += " ";
        }
        return result.stripTrailing();
    }
}*/
/*
public class ReverseWords {
    public static String reverseWords(String str) {
        String[] words = str.split(" ");
        String result = "";
        for (int i = 0; i < words.length; i++) {
            result += words[words.length - i - 1];
            result += " ";
        }
        return result.stripTrailing();
    }
}
*/

import java.util.Arrays;

public class ReverseWords {
    public static String reverseWords(String str) {
        return Arrays.stream(str.split(" ")).reduce((x, y) -> y + " " + x).get();
    }
}
