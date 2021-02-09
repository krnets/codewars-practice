using NUnit.Framework;
using System;
using System.Collections.Generic;

[TestFixture]
public class Sample_Test
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new int[,] {{1, 0}, {0, 0}}).Returns(new Tuple<int, int>(0, 0));
            yield return new TestCaseData(new int[,] {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}).Returns(
                new Tuple<int, int>(0, 0));
            yield return new TestCaseData(new int[,] {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}}).Returns(
                new Tuple<int, int>(2, 2));
            yield return new TestCaseData(new int[,] {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}}).Returns(
                new Tuple<int, int>(-1, -1));
        }
    }

    [Test, TestCaseSource("testCases")]
    public Tuple<int, int> Test(int[,] field) => Kata.MineLocation(field);
}

[TestFixture]
public class Random_Test
{
    private static Random rnd = new Random();

    private static Tuple<int, int> solution(int[,] field)
    {
        for (int i = 0; i < field.GetLength(0); ++i)
        {
            for (int j = 0; j < field.GetLength(1); ++j)
            {
                if (field[i, j] == 1)
                {
                    return new Tuple<int, int>(i, j);
                }
            }
        }

        return null;
    }

    [Test]
    public void RandomTests()
    {
        const int Tests = 100;

        for (int i = 0; i < Tests; ++i)
        {
            int size = rnd.Next(3, 20);
            int[,] test = new int[size, size];

            for (int j = 0; j < size; ++j)
            {
                for (int k = 0; k < size; ++k)
                {
                    test[j, k] = 0;
                }
            }

            test[rnd.Next(0, size), rnd.Next(0, size)] = 1;

            Tuple<int, int> expected = solution(test);
            Tuple<int, int> actual = Kata.MineLocation(test);

            Assert.AreEqual(expected, actual);
        }
    }
}