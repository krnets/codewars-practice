# 7kyu - Common Substrings

""" Given 2 strings, your job is to find out if there is a substring that appears in both strings. 
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

# Output: A boolean value determining if there is a common substing between the two inputs. """


# def substring_test(s1, s2):
#     s1 = s1.lower()
#     s2 = s2.lower()
#     for i in range(len(s1)):
#         for j in range(i+2, len(s1)):
#             if s1[i:j] in s2:
#                 return True
#     return False

def substring_test(a, b):
    a, b = a.lower(), b.lower()
    if len(a) > len(b): a, b = b, a
    return any(a[i:i+2] in b for i in range(len(a)-1))


q = substring_test("Something", "Home")  # True
q
q = substring_test("Something", "Fun")  # False
q
q = substring_test("Something", "")  # False
q
q = substring_test("", "Something")  # False
q
q = substring_test("BANANA", "banana")  # True
q
q = substring_test("test", "lllt")  # False
q
q = substring_test("", "")  # False
q
q = substring_test("1234567", "541265")  # True
q
q = substring_test("supercalifragilisticexpialidocious",
                   "SoundOfItIsAtrocious")  # True
q
q = substring_test("LoremipsumdolorsitametconsecteturadipiscingelitAeneannonaliquetligulautplaceratorciSuspendissepotentiMorbivolutpatauctoripsumegetaliquamPhasellusidmagnaelitNullamerostellustemporquismolestieaornarevitaediamNullaaliquamrisusnonviverrasagittisInlaoreetultricespretiumVestibulumegetnullatinciduntsempersemacrutrumfelisPraesentpurusarcutempusnecvariusidultricesaduiPellentesqueultriciesjustolobortisrhoncusdignissimNuncviverraconsequatblanditUtbibendumatlacusactristiqueAliquamimperdietnuncsempertortorefficiturviverra", "thisisalongstringtest")  # True
q
