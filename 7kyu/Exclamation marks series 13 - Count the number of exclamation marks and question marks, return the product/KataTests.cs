using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void MyTest()
    {
        Assert.AreEqual(0, Kata.Product(""));
        Assert.AreEqual(1, Kata.Product("!?"));
        Assert.AreEqual(2, Kata.Product("!??"));
        Assert.AreEqual(2, Kata.Product("!!?"));
        Assert.AreEqual(6, Kata.Product("!!???"));
        Assert.AreEqual(6, Kata.Product("!!!??"));
        Assert.AreEqual(4, Kata.Product("!!??"));
        Assert.AreEqual(4, Kata.Product("!????"));
        Assert.AreEqual(4, Kata.Product("!!!!?"));
        Assert.AreEqual(5, Kata.Product("!?????"));
        Assert.AreEqual(20, Kata.Product("!!????!!?"));
        Assert.AreEqual(49, Kata.Product("!!???????!!!!!"));
        Assert.AreEqual(165, Kata.Product("!!???????????!!!!!?!?!?!?!"));
        Assert.AreEqual(4, Kata.Product("!!aabbcc??"));
        Assert.AreEqual(4, Kata.Product("! !aa bb   c c??   "));
    }
}