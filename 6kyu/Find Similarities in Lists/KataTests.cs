using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public class MyTest
{
    [Test]
    public void FirstTest()
    {
        List<int> first = new List<int>() {1, 2, 3, 4, 5, 6};
        List<int> second = new List<int>() {5, 7, 8, 0, 2, 3, 4, 10};
        int n = 2;
        StringAssert.AreEqualIgnoringCase("2,3 | 3,4", Kata.AnySimilarity(first, second, n));
    }

    [Test]
    public void SecondTest()
    {
        List<int> first = new List<int>() {1, 2, 3, 4, 5, 6};
        List<int> second = new List<int>() {5, 7, 8, 0, 2, 3, 4, 10};
        int n = 3;
        StringAssert.AreEqualIgnoringCase("2,3,4", Kata.AnySimilarity(first, second, n));
    }
}