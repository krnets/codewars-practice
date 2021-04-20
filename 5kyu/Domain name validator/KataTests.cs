using NUnit.Framework;

[TestFixture]
public class DomainNameValidatorTest
{
    DomainNameValidator v = new DomainNameValidator();

    [Test]
    public void DomainTest1()
    {
        Assert.AreEqual(false, v.validate("codewars"));
    }

    [Test]
    public void DomainTest2()
    {
        Assert.AreEqual(true, v.validate("g.co"));
    }

    [Test]
    public void DomainTest3()
    {
        Assert.AreEqual(true, v.validate("codewars.com"));
    }

    [Test]
    public void DomainTest4()
    {
        Assert.AreEqual(true, v.validate("CODEWARS.COM"));
    }

    [Test]
    public void DomainTest5()
    {
        Assert.AreEqual(true, v.validate("sub.codewars.com"));
    }

    [Test]
    public void DomainTest6()
    {
        Assert.AreEqual(false, v.validate("codewars.com-"));
    }

    [Test]
    public void DomainTest7()
    {
        Assert.AreEqual(false, v.validate(".codewars.com"));
    }

    [Test]
    public void DomainTest8()
    {
        Assert.AreEqual(false, v.validate("example@codewars.com"));
    }

    [Test]
    public void DomainTest9()
    {
        Assert.AreEqual(false, v.validate("127.0.0.1"));
    }
}