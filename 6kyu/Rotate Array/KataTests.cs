using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void BasicTest1()
    {
        var data = new object[] {1, 2, 3, 4, 5};

        Assert.AreEqual(new object[] {5, 1, 2, 3, 4}, Kata.Rotate(data, 1));
        Assert.AreEqual(new object[] {4, 5, 1, 2, 3}, Kata.Rotate(data, 2));
        Assert.AreEqual(new object[] {3, 4, 5, 1, 2}, Kata.Rotate(data, 3));
        Assert.AreEqual(new object[] {2, 3, 4, 5, 1}, Kata.Rotate(data, 4));
        Assert.AreEqual(new object[] {1, 2, 3, 4, 5}, Kata.Rotate(data, 5));
    }

    [Test]
    public void BasicTest2()
    {
        var data = new object[] {1, 2, 3, 4, 5};
        Assert.AreEqual(new object[] {1, 2, 3, 4, 5}, Kata.Rotate(data, 0));
    }

    [Test]
    public void BasicTest3()
    {
        var data = new object[] {1, 2, 3, 4, 5};
        Assert.AreEqual(new object[] {2, 3, 4, 5, 1}, Kata.Rotate(data, -1));
        Assert.AreEqual(new object[] {3, 4, 5, 1, 2}, Kata.Rotate(data, -2));
        Assert.AreEqual(new object[] {4, 5, 1, 2, 3}, Kata.Rotate(data, -3));
        Assert.AreEqual(new object[] {5, 1, 2, 3, 4}, Kata.Rotate(data, -4));
        Assert.AreEqual(new object[] {1, 2, 3, 4, 5}, Kata.Rotate(data, -5));
    }

    [Test]
    public void BasicTest4()
    {
        var data = new object[] {1, 2, 3, 4, 5};
        Assert.AreEqual(new object[] {'c', 'a', 'b'}, Kata.Rotate(new object[] {'a', 'b', 'c'}, 1));
    }

    [Test]
    public void BasicTest5()
    {
        var data = new object[] {1, 2, 3, 4, 5};
        Assert.AreEqual(new object[] {3.0, 1.0, 2.0}, Kata.Rotate(new object[] {1.0, 2.0, 3.0}, 1));
    }

    [Test]
    public void BasicTest6()
    {
        var data = new object[] {1, 2, 3, 4, 5};
        Assert.AreEqual(new object[] {false, true, true}, Kata.Rotate(new object[] {true, true, false}, 1));
    }

    [Test]
    public void BasicTest7()
    {
        var data = new object[] {1, 2, 3, 4, 5};

        Assert.AreEqual(new object[] {4, 5, 1, 2, 3}, Kata.Rotate(data, 7));
        Assert.AreEqual(new object[] {5, 1, 2, 3, 4}, Kata.Rotate(data, 11));
        Assert.AreEqual(new object[] {3, 4, 5, 1, 2}, Kata.Rotate(data, 12478));
    }
}