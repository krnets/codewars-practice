using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void Test1()
    {
        Assert.IsTrue(Kata.ValidPhoneNumber("(123) 456-7890"));
    }

    [Test]
    public void Test2()
    {
        Assert.IsFalse(Kata.ValidPhoneNumber("(1111)5X5 2345"));
    }
}