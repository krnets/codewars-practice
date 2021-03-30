using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        int[][] matrix = new int[][]
        {
            new int[] {1, 2, 3},
            new int[] {4, 5, 6},
            new int[] {7, 8, 9}
        };
        Assert.That(Kata.LargestCrossSum(matrix), Is.EqualTo(33));
        matrix = new int[][]
        {
            new int[] {1, 2, 1},
            new int[] {2, 2, 2},
            new int[] {1, 2, 1}
        };
        Assert.That(Kata.LargestCrossSum(matrix), Is.EqualTo(10));
        matrix = new int[][]
        {
            new int[] {1, 2, 1, 1},
            new int[] {2, 2, 2, 2},
            new int[] {1, 2, 1, 2},
            new int[] {1, 2, 1, 1}
        };
        Assert.That(Kata.LargestCrossSum(matrix), Is.EqualTo(14));
        matrix = new int[][]
        {
            new int[] {1, 1, 1, 4, 1, 1, 1},
            new int[] {3, 3, 3, 3, 3, 3, 3},
            new int[] {1, 1, 1, 4, 1, 1, 1}
        };
        Assert.That(Kata.LargestCrossSum(matrix), Is.EqualTo(29));
    }
}