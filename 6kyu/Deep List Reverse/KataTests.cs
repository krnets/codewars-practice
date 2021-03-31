using NUnit.Framework;
using System.Linq;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        var input = new object[] {1, 2};
        var expected = new object[] {2, 1};
        Assert.AreEqual(AsString(expected), AsString(Kata.DeepReverse(input)));
    }

    [Test]
    public void BasicTest2()
    {
        var input = new object[] {new object[] {6, 5}, new object[] {4, 3}};
        var expected = new object[] {new object[] {3, 4}, new object[] {5, 6}};
        Assert.AreEqual(AsString(expected), AsString(Kata.DeepReverse(input)));
    }

    [Test]
    public void BasicTest3()
    {
        var input = new object[] {new object[] {1, 2, 3}, new object[] {4, 5, 6}, new object[] {7, 8, 9}};
        var expected = new object[] {new object[] {9, 8, 7}, new object[] {6, 5, 4}, new object[] {3, 2, 1}};
        Assert.AreEqual(AsString(expected), AsString(Kata.DeepReverse(input)));
    }

    [Test]
    public void BasicTest4()
    {
        var input = new object[]
        {
            new object[] {110, 109, 108}, new object[] {107, 106, 105}, new object[] {104, 103, 102},
            new object[] {101, 100}
        };
        var expected = new object[]
        {
            new object[] {100, 101}, new object[] {102, 103, 104}, new object[] {105, 106, 107},
            new object[] {108, 109, 110}
        };
        Assert.AreEqual(AsString(expected), AsString(Kata.DeepReverse(input)));
    }

    [Test]
    public void BasicTest5()
    {
        var input = new object[]
            {new object[] {50, 51, new object[] {52, 53}}, new object[] {new object[] {54, 55}, 56, 57}};
        var expected = new object[]
            {new object[] {57, 56, new object[] {55, 54}}, new object[] {new object[] {53, 52}, 51, 50}};
        Assert.AreEqual(AsString(expected), AsString(Kata.DeepReverse(input)));
    }

    [Test]
    public void BasicTest6()
    {
        var input = new object[]
        {
            1000, 1001, 1002, 1003,
            new object[] {1004, new object[] {1005, 1006, 1007, new object[] {1008, 1009, 1010}}},
            new object[] {1011}, new object[] {1012, 1013, 1014}, new object[] {1015, 1016, 1017}
        };
        var expected = new object[]
        {
            new object[] {1017, 1016, 1015}, new object[] {1014, 1013, 1012}, new object[] {1011},
            new object[] {new object[] {new object[] {1010, 1009, 1008}, 1007, 1006, 1005}, 1004}, 1003, 1002, 1001,
            1000
        };
        Assert.AreEqual(AsString(expected), AsString(Kata.DeepReverse(input)));
    }

    private string AsString(object[] o)
    {
        if (o == null)
        {
            return "[null]";
        }

        return "[" + string.Join(",", o.Select(a => a.GetType().IsArray ? AsString((object[]) a) : a)) + "]";
    }
}