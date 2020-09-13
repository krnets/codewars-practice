/*
Given 2 strings, your job is to find out if there is a substring that appears in both strings.
You will return true if you find a substring that appears in both strings, or false if you do not.
We only care about substrings that are longer than one letter long.

Example 1
            SubstringTest("Something","Fun"); => false

            The method will return false because something and fun contain
            no common substrings.
            (We do not count the 'n' as a substring in this Kata because it is only

Example 2
            SubstringTest("Something","Home"); => true

            Returns true because both of the inputs contain the substring "me".
            (soMEthing and hoME)
            1 character long)

Rules:      Lowercase and uppercase letters are the same. So 'A' == 'a'.
            We only count substrings that are > 1 in length.

Input:      Two strings with both lower and upper cases.
Output:     A boolean value determining if there is a common substring between the two inputs.
*/

public class Kata {
    public static boolean SubstringTest(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        for (int i = 0; i < str1.length() - 1; i++)
            if (str2.contains(str1.substring(i, i + 2)))
                return true;

        return false;
    }
}