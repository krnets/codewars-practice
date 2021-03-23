using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class BasicTest
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData("apple").Returns(new List<char> {'p'});
            yield return new TestCaseData("limbojackassin the garden").Returns(new List<char>
                {'a', 's', 'i', ' ', 'e', 'n'});
            yield return new TestCaseData("11pinguin").Returns(new List<char> {'1', 'i', 'n'});
        }
    }

    [Test, TestCaseSource("testCases")]
    public List<char> Test(string str)
    {
        return Kata.Remember(str);
    }
}