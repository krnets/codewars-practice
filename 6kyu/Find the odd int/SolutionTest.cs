using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(5, Kata.find_it(new[] {20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5}));
    }


    [Test]
    public void Test2()
    {
        Assert.AreEqual(5, Kata.find_it(new[] {20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5}));
    }


    [Test]
    public void Test3()
    {
        Assert.AreEqual(-1, Kata.find_it(new[] {1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5}));
    }


    [Test]
    public void Test4()
    {
        Assert.AreEqual(5, Kata.find_it(new[] {20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5}));
    }


    [Test]
    public void Test5()
    {
        Assert.AreEqual(10, Kata.find_it(new[] {10}));
    }


    [Test]
    public void Test6()
    {
        Assert.AreEqual(10, Kata.find_it(new[] {1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1}));
    }


    [Test]
    public void Test7()
    {
        Assert.AreEqual(1, Kata.find_it(new[] {5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10}));
    }
}