using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class Sample_Tests
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData("abcdeb", "b").Returns(2);
            yield return new TestCaseData("abcdeb", "a").Returns(1);
            yield return new TestCaseData("ccddeeccddeecc", "cc").Returns(3);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int SampleTest(string fullText, string searchText) => Kata.SubstringCount(fullText, searchText);
}