using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class Test
{
    [Test]
    public void MissingNumberTest()
    {
        Assert.AreEqual(6,
            Kata.FindDeletedNumber(new List<int>() {1, 2, 3, 4, 5, 6, 7, 8, 9},
                new List<int>() {5, 7, 1, 9, 4, 8, 2, 3}));
        Assert.AreEqual(1, Kata.FindDeletedNumber(new List<int>() {1}, new List<int>()));
    }

    [Test]
    public void NoMissingNumberTest()
    {
        Assert.AreEqual(0,
            Kata.FindDeletedNumber(new List<int>() {1, 2, 3, 4, 5, 6, 7}, new List<int>() {2, 3, 6, 1, 5, 4, 7}));
        Assert.AreEqual(0,
            Kata.FindDeletedNumber(new List<int>() {1, 2, 3, 4, 5, 6, 7, 8, 9},
                new List<int>() {5, 7, 6, 9, 4, 8, 1, 2, 3}));
    }

    [Test]
    public void NilTest()
    {
        Assert.AreEqual(0, Kata.FindDeletedNumber(new List<int>(), new List<int>()));
    }
}