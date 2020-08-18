/*
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_').

        StringSplit.solution("abc") // should return {"ab", "c_"}
        StringSplit.solution("abcdef") // should return {"ab", "cd", "ef"}
*/

import java.util.ArrayList;

/*
public class StringSplit {
    public static String[] solution(String s) {
        var list = new ArrayList<String>();
        s += '_';

        for (int i = 0; i < s.length() - 1; i += 2)
            list.add(s.substring(i, i + 2));

        var result = new String[list.size()];

        for (int i = 0; i < result.length; i++)
            result[i] = list.get(i);

        return result;
    }
}*/

/*
public class StringSplit {
    public static String[] solution(String s) {
        var list = new ArrayList<String>();
        s += '_';

        for (int i = 0; i < s.length() - 1; i += 2)
            list.add(s.substring(i, i + 2));

        return list.toArray(new String[0]);
    }
}
*/

public class StringSplit {
    public static String[] solution(String s) {
        s = (s.length() % 2 == 0 ? s : s + '_');
        return s.split("(?<=\\G.{2})");
    }
}
