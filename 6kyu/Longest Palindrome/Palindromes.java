/*
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”,
the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

        "a" -> 1
        "aab" -> 2
        "abcde" -> 1
        "zzbaabcd" -> 4
        "" -> 0
*/

public class Palindromes {
    public static int longestPalindrome(final String s) {
        int longest = 0;

        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                String slice = s.substring(i, j);

                if (isPalindrome(slice))
                    longest = Math.max(longest, slice.length());
            }
        }
        return s.isEmpty() ? 0 : longest;
    }

    private static boolean isPalindrome(String str) {
        return new StringBuilder(str).reverse().toString().equals(str);
    }
}