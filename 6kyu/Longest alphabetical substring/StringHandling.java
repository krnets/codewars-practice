/*
Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

There are tests with strings up to 10 000 characters long so your code will need to be efficient.

The input will only consist of lowercase characters and will be at least one letter long.

If there are multiple solutions, return the one that appears first.
*/

class StringHandling {
    public static String longestAlpabeticalSubstring(String text) {
        int pos = 0, max = 0, current = 0;

        for (int i = 1; i < text.length(); i++) {
            if (text.charAt(i - 1) <= text.charAt(i)) {
                current++;
                if (current > max) {
                    max = current;
                    pos = i - max;
                }
            } else {
                current = 0;
            }
        }
        return text.substring(pos, pos + max + 1);
    }
}