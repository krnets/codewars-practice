/*
You will be given a string and you task is to check if it is possible
to convert that string into a palindrome by removing a single character.
If the string is already a palindrome, return "OK".

If it is not, and we can convert it to a palindrome by removing one character,
then return "remove one", otherwise return "not possible".
The order of the characters should not be changed.

For example:

        solve("abba") = "OK". -- This is a palindrome
        solve("abbaa") = "remove one". -- remove the 'a' at the extreme right.
        solve("abbaab") = "not possible".

*/


class Solution {
    public static String solve(String s) {
        if (Solution.isPalindrome(s))
            return "OK";

        for (int i = 0; i < s.length(); i++) {
//            var oneCharRemoved = s.substring(0, i) + s.substring(i + 1);
            var oneCharRemoved = new StringBuilder(s).deleteCharAt(i).toString();

            if (isPalindrome(oneCharRemoved))
                return "remove one";
        }
        return "not possible";
    }

    private static boolean isPalindrome(String s) {
        return new StringBuilder(s).reverse().toString().equals(s);
    }
}