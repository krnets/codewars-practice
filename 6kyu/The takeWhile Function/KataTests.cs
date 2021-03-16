using NUnit.Framework;
using System;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Func<int, bool> isEven = (num) => num % 2 == 0;
        Func<int, bool> isOdd = (num) => num % 2 != 0;

        Assert.AreEqual(new int[0], Kata.TakeWhile(new int[0], isEven));
        Assert.AreEqual(new int[] {2, 6, 4, 10}, Kata.TakeWhile(new int[] {2, 6, 4, 10, 1, 5, 4, 3}, isEven));
        Assert.AreEqual(new int[] {2, 100, 1000, 10000},
            Kata.TakeWhile(new int[] {2, 100, 1000, 10000, 5, 3, 4, 6}, isEven));
        Assert.AreEqual(new int[] {998, 996, 12, -1000, 200, 0},
            Kata.TakeWhile(new int[] {998, 996, 12, -1000, 200, 0, 1, 1, 1}, isEven));
        Assert.AreEqual(new int[] { }, Kata.TakeWhile(new int[] {1, 4, 2, 3, 5, 4, 5, 6, 7}, isEven));
        Assert.AreEqual(new int[] {2, 4, 10, 100, 64, 78, 92},
            Kata.TakeWhile(new int[] {2, 4, 10, 100, 64, 78, 92}, isEven));

        Assert.AreEqual(new int[] {1, 5, 111, 1111},
            Kata.TakeWhile(new int[] {1, 5, 111, 1111, 2, 4, 1, 6, 4, 5}, isOdd));
        Assert.AreEqual(new int[] {-1, -5, 127}, Kata.TakeWhile(new int[] {-1, -5, 127, 86, 5, 7, 902, 2, 1}, isOdd));
        Assert.AreEqual(new int[] { }, Kata.TakeWhile(new int[] {2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0}, isOdd));
        Assert.AreEqual(new int[] {1, 3, 5, 7, 9, 111}, Kata.TakeWhile(new int[] {1, 3, 5, 7, 9, 111}, isOdd));
    }
}