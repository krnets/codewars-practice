using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class Sample_Test
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new[] {new int[] {1, 1, 2, 3}}).Returns(1);
            yield return new TestCaseData(new[] {new int[] {5, 4, 3, 2, 1, 1}}).Returns(1);
            yield return new TestCaseData(new[] {new int[] {1, 3, 2, 5, 4, 5, 7, 6}}).Returns(5);
            yield return new TestCaseData(new[] {new int[] {8, 2, 6, 3, 7, 2, 5, 1, 4}}).Returns(2);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int Test(int[] arr) => Kata.FindDup(arr);
}