using NUnit.Framework;
using System.Collections.Generic;

[TestFixture, Description("Tests")]
public class GetSlopeTest
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new Point(1, 1), new Point(2, 2)).Returns(1)
                .SetDescription("Should calculate the existing non-zero between 2 points");
            yield return new TestCaseData(new Point(11, 1), new Point(1, 11)).Returns(-1)
                .SetDescription("Should calculate the existing non-zero between 2 points");

            yield return new TestCaseData(new Point(1, 1), new Point(1, 2)).Returns(null)
                .SetDescription("Should return null if the line passing through the points is vertical");

            yield return new TestCaseData(new Point(1, 1), new Point(1, 1)).Returns(null)
                .SetDescription("Should return null if the same point is given twice");
        }
    }

    [Test, TestCaseSource("testCases")]
    public double? Test(Point p1, Point p2) =>
        Kata.GetSlope(p1, p2);
}