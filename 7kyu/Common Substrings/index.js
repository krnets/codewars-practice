// 7kyu - Common Substrings

/* Given 2 strings, your job is to find out if there is a substring that appears in both strings. 
You will return true if you find a substring that appears in both strings, or false if you do not. 
We only care about substrings that are longer than one letter long.

# Examples:

*Example 1*
SubstringTest("Something","Fun"); //Returns false

*Example 2*
SubstringTest("Something","Home"); //Returns true

In the above example, example 2 returns true because both of the inputs contain the substring "me". 
(soMEthing and hoME)

In example 1, the method will return false because something and fun contain no common substrings. 
(We do not count the 'n' as a substring in this Kata because it is only 1 character long)

# Rules: Lowercase and uppercase letters are the same. So 'A' == 'a'.
We only count substrings that are > 1 in length.

# Input: Two strings with both lower and upper cases.
# Output: A boolean value determining if there is a common substing between the two inputs.  */


function SubstringTest(str1, str2) {
    let s1 = str1.toLowerCase()
    let s2 = str2.toLowerCase()

    if (s1.length > s2.length)
        [s1, s2] = [s2, s1]

    for (let i = 0; i < s1.length - 1; i++)
        if (s2.includes(s1.slice(i, i + 2)))
            return true
    return false
}

q = SubstringTest("Something", "Home") // true
q
q = SubstringTest("Something", "Fun") // false
q
q = SubstringTest("Something", "") // false
q
q = SubstringTest("", "Something") // false
q
q = SubstringTest("BANANA", "banana") // true
q
q = SubstringTest("test", "lllt") // false
q
q = SubstringTest("", "") // false
q
q = SubstringTest("1234567", "541265") // true
q
q = SubstringTest("supercalifragilisticexpialidocious", "SoundOfItIsAtrocious") // true
q