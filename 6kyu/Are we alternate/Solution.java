/*
Create a function isAlt() that accepts a string as an argument and validates whether the vowels
(a, e, i, o, u) and consonants are in alternate order.

        isAlt("amazon") // true
        isAlt("apple")  // false
        isAlt("banana") // true

        Arguments consist of only lowercase letters.
*/

/*
public class Solution {
    public static boolean isAlt(String word) {
        String vowels = "[aeiou]";
        boolean isFirstLetterVowel = word.substring(0, 1).matches(vowels);

        for (int i = 0; i < word.length(); i++) {
            var c = word.substring(i, i + 1);

            if (isFirstLetterVowel) {
                if (i % 2 == 0 && !vowels.contains(c)) return false;
                if (i % 2 != 0 && vowels.contains(c)) return false;
            } else {
                if (i % 2 == 0 && vowels.contains(c)) return false;
                if (i % 2 != 0 && !vowels.contains(c)) return false;
            }
        }
        return true;
    }
}*/

public class Solution {
    public static boolean isAlt(String word) {
        String vowels = "aeiou";
        boolean isVowel = vowels.contains(word.substring(0, 1));

        for (int i = 1; i < word.length(); i++) {
            if (vowels.contains(word.substring(i, i + 1)) == isVowel) {
                return false;
            }
            isVowel = !isVowel;
        }
        return true;
    }
}

/*
public class Solution {
    public static boolean isAlt(String word) {
        return word.matches("[aeiou]?([^aeiou][aeiou])*[^aeiou]?");
    }
}
*/

/*
public class Solution {
    public static boolean isAlt(String word) {
        return !word.matches(".*[aeiou]{2}.*|.*[^aeiou]{2}.*");
    }
}
*/
