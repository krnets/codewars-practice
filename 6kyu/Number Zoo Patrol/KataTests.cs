using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class Sample_Test
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new[] {new int[] {1, 3, 4, 5, 6, 7, 8}}).Returns(2);
            yield return new TestCaseData(new[] {new int[] {7, 8, 1, 2, 4, 5, 6}}).Returns(3);
            yield return new TestCaseData(new[] {new int[] {1, 2, 3, 5}}).Returns(4);
            yield return new TestCaseData(new[] {new int[] {1, 2}}).Returns(3);
            yield return new TestCaseData(new[] {new int[] { }}).Returns(1);
            yield return new TestCaseData(new[] {new int[] {2, 3, 4}}).Returns(1);
            yield return new TestCaseData(new[] {new int[] {13, 11, 10, 3, 2, 1, 4, 5, 6, 9, 7, 8}}).Returns(12);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int Test(int[] array) => Kata.FindNumber(array);
}