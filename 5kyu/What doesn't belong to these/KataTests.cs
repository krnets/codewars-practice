using NUnit.Framework;

public class KataTests
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(1, Kata.FindTheNotFittingElement(new object[] {1, 2, 2, 2, 2}));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(false, Kata.FindTheNotFittingElement(new object[] {true, true, true, false, true}));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual('b', Kata.FindTheNotFittingElement(new object[] {'a', 'a', 'b', 'a', 'a', 'a', 'a'}));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(2, Kata.FindTheNotFittingElement(new object[] {'1', 2, '4', '6', '8'}));
    }

    [Test]
    public void ExampleTest5()
    {
        Assert.AreEqual('2', Kata.FindTheNotFittingElement(new object[] {2, 2, 2, 2, 2, '2'}));
    }

    [Test]
    public void ExampleTest6()
    {
        Assert.AreEqual(true, Kata.FindTheNotFittingElement(new object[] {1, 2, 4, 6, true}));
    }

    [Test]
    public void ExampleTest7()
    {
        Assert.AreEqual(1, Kata.FindTheNotFittingElement(new object[] {1, 2, 4, 6, 10}));
    }

    [Test]
    public void ExampleTest8()
    {
        Assert.AreEqual(-2, Kata.FindTheNotFittingElement(new object[] {2, 2, -2, 6, 10}));
    }

    [Test]
    public void ExampleTest9()
    {
        Assert.AreEqual('t', Kata.FindTheNotFittingElement(new object[] {'Z', 'L', 'P', 't', 'G'}));
    }

    [Test]
    public void ExampleTest10()
    {
        Assert.AreEqual('3', Kata.FindTheNotFittingElement(new object[] {'Z', 'L', '3', 't', 'G'}));
    }

    [Test]
    public void ExampleTest11()
    {
        Assert.AreEqual(4, Kata.FindTheNotFittingElement(new object[] {'Z', 'L', '3', 't', 4}));
    }

    [Test]
    public void ExampleTest12()
    {
        Assert.AreEqual('.', Kata.FindTheNotFittingElement(new object[] {'Z', 'e', '.', 'a', 'G'}));
    }
}