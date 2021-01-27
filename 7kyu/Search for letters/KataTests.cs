using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class Fixed_Test
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData("a **&  bZ")
                .Returns("11000000000000000000000001");
            yield return new TestCaseData("!!a$%&RgTT")
                .Returns("10000010000000000101000000");
            yield return new TestCaseData("")
                .Returns("00000000000000000000000000")
                .SetDescription("Empty string should return 26 '0'");
            yield return new TestCaseData("abcdefghijklmnopqrstuvwxyz")
                .Returns("11111111111111111111111111");
            yield return new TestCaseData("aaaaaaaaaaa")
                .Returns("10000000000000000000000000");
            yield return new TestCaseData("&%&%/$%$%$%$%GYtf67fg34678hgfdyd")
                .Returns("00010111000000000001000010");
        }
    }

    [Test, TestCaseSource("testCases")]
    public string Test(string input) => Kata.Change(input);
}