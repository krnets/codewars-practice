using NUnit.Framework;
using System.Linq;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest()
    {
        Assert.AreEqual(new[] {1, 9, 6, 3, 0, 1, 1, 1, 1, 1},
            Kata.PaintLetterBoxes(125, 132).ToArray());
    }
}