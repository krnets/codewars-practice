using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        var bigArray = new object[][]
        {
            new object[] {2, 3}, new object[] {7, 2}, new object[] {9, 20}, new object[] {1, 2}, new object[] {7, 2},
            new object[] {45, 4}, new object[] {7, 87}, new object[] {4, 5}, new object[] {2, 7}, new object[] {6, 32}
        };

        var searchFor = new object[] {9, 20};
        Assert.AreEqual(2, Kata.SearchArray(bigArray, searchFor));
    }

    [Test]
    public void BasicTest2()
    {
        var bigArray = new object[][]
        {
            new object[] {2, 3}, new object[] {7, 2}, new object[] {9, 20}, new object[] {1, 2}, new object[] {7, 2},
            new object[] {45, 4}, new object[] {7, 87}, new object[] {4, 5}, new object[] {2, 7}, new object[] {6, 32}
        };

        var searchFor = new object[] {1, 12};
        Assert.AreEqual(-1, Kata.SearchArray(bigArray, searchFor));
    }

    [Test]
    public void BasicTest3()
    {
        var bigArray = new object[][]
        {
            new object[] {2, 3}, new object[] {7, 2}, new object[] {9, 20}, new object[] {1, 2}, new object[] {7, 2},
            new object[] {45, 4}, new object[] {7, 87}, new object[] {4, 5}, new object[] {2, 7}, new object[] {6, 32}
        };

        var searchFor = new object[] {7, 2};
        Assert.AreEqual(1, Kata.SearchArray(bigArray, searchFor));
    }
}