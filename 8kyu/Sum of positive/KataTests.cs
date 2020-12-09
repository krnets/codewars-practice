using NUnit.Framework;
using System;
using System.Linq;

[TestFixture]
public class Tests
{
    [Test]
    [TestCase(new int[] {1, 2, 3, 4, 5}, ExpectedResult = 15)]
    [TestCase(new int[] {1, -2, 3, 4, 5}, ExpectedResult = 13)]
    [TestCase(new int[] {-1, 2, 3, 4, -5}, ExpectedResult = 9)]
    [TestCase(new int[] { }, ExpectedResult = 0)]
    [TestCase(new int[] {-1, -2, -3, -4, -5}, ExpectedResult = 0)]
    public static int ExampleTest(int[] arr)
    {
        return Kata.PositiveSum(arr);
    }

    [Test]
    public static void RandomTest([Random(5, 120, 40)] int length)
    {
        int[] arr = RandomArray(length);
        Assert.AreEqual(Solution(arr), Kata.PositiveSum(arr), string.Format("Failed when arr = {0}", arr));
    }

    public static int[] RandomArray(int length)
    {
        int[] result = new int[length];
        Random rnd = new Random();
        for (int i = 0; i < length; ++i)
        {
            result[i] = rnd.Next(-100, 100);
        }

        return result;
    }

    private static int Solution(int[] arr)
    {
        return arr.Where(x => x > 0).Sum();
    }
}