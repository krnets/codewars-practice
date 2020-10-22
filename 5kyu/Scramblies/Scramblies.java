/*
Complete the function scramble(str1, str2) that returns true
if a portion of str1 characters can be rearranged to match str2,
otherwise returns false.

Notes:  Only lower case letters will be used (a-z). No punctuation or digits will be included.
        Performance needs to be considered

        Input strings s1 and s2 are null terminated.

        scramble('rkqodlw', 'world') ==> True
        scramble('cedewaraaossoqqyt', 'codewars') ==> True
        scramble('katas', 'steak') ==> False
*/


import java.util.Map;
import java.util.stream.Collectors;

public class Scramblies {
    public static boolean scramble(String str1, String str2) {
        var freqMap1 = str1.chars().boxed().collect(Collectors.groupingBy(i -> i, Collectors.counting()));
        var freqMap2 = str2.chars().boxed().collect(Collectors.groupingBy(i -> i, Collectors.counting()));
        int charCount = 0;

        for (Map.Entry<Integer, Long> e : freqMap2.entrySet()) {
            if (freqMap1.containsKey(e.getKey()) && freqMap1.get(e.getKey()) >= e.getValue())
                charCount++;
        }
        return charCount == freqMap2.size();
    }
}

/*
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class Scramblies {
    public static boolean scramble(String str1, String str2) {
        var chars1 = str1.chars().boxed().collect(Collectors.toList());
        var chars2 = str2.chars().boxed().collect(Collectors.toList());

        for (Integer c : chars2) {
            if (!chars1.remove(c))
                return false;
        }
        return true;
    }
}
*/
