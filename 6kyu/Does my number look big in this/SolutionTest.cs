using System;
using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;

[TestFixture]
public class SolutionTest
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(1)
                .Returns(true)
                .SetDescription("1 is narcissitic");
            yield return new TestCaseData(371)
                .Returns(true)
                .SetDescription("371 is narcissitic");
        }
    }

    [Test, TestCaseSource("testCases")]
    public bool Test(int n) => Kata.Narcissistic(n);


    [TestFixture]
    public class Small_Number_Test
    {
        private static IEnumerable<TestCaseData> testCases
        {
            get
            {
                yield return new TestCaseData(1)
                    .Returns(true)
                    .SetDescription("1 is narcissitic");
                yield return new TestCaseData(5)
                    .Returns(true)
                    .SetDescription("5 is narcissitic");
                yield return new TestCaseData(7)
                    .Returns(true)
                    .SetDescription("7 is narcissitic");
            }
        }

        [Test, TestCaseSource("testCases")]
        public bool Test(int n) => Kata.Narcissistic(n);
    }

    [TestFixture]
    public class Narcissistic_Number_Test
    {
        private static IEnumerable<TestCaseData> testCases
        {
            get
            {
                yield return new TestCaseData(153)
                    .Returns(true)
                    .SetDescription("153 is narcissitic");
                yield return new TestCaseData(370)
                    .Returns(true)
                    .SetDescription("370 is narcissitic");
                yield return new TestCaseData(371)
                    .Returns(true)
                    .SetDescription("371 is narcissitic");
                yield return new TestCaseData(1634)
                    .Returns(true)
                    .SetDescription("1634 is narcissitic");
            }
        }

        [Test, TestCaseSource("testCases")]
        public bool Test(int n) => Kata.Narcissistic(n);
    }

    [TestFixture]
    public class Not_Narcissistic_Number_Test
    {
        private static IEnumerable<TestCaseData> testCases
        {
            get
            {
                yield return new TestCaseData(154)
                    .Returns(false)
                    .SetDescription("154 is not narcissitic");
                yield return new TestCaseData(378)
                    .Returns(false)
                    .SetDescription("378 is not narcissitic");
                yield return new TestCaseData(999)
                    .Returns(false)
                    .SetDescription("999 is not narcissitic");
            }
        }

        [Test, TestCaseSource("testCases")]
        public bool Test(int n) => Kata.Narcissistic(n);
    }

    [TestFixture]
    public class Random_Number_Test
    {
        private static Random rnd = new();

        private static List<int> nNums = new()
        {
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725,
            4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153
        };

        [Test, Description("Random Tests")]
        public void RandomTest()
        {
            const int Tests = 200;

            for (int i = 0; i < Tests; ++i)
            {
                if (rnd.Next(0, 2) == 0)
                    Assert.That(Kata.Narcissistic(nNums[rnd.Next(0, nNums.Count())]));
                else
                {
                    int num = rnd.Next();
                    Assert.AreEqual(nNums.Contains(num), Kata.Narcissistic(num));
                }
            }
        }
    }
}