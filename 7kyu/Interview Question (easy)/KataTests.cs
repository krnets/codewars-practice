using NUnit.Framework;

[TestFixture]
public class GetStringsTest
{
    [Test]
    public void GenericTest1()
    {
        Assert.AreEqual("c:**,h:*,i:*,a:*,g:*,o:*", Kata.GetStrings("Chicago"));
    }

    [Test]
    public void GenericTest2()
    {
        Assert.AreEqual("b:*,a:*,n:*,g:*,k:**,o:*", Kata.GetStrings("Bangkok"));
    }

    [Test]
    public void GenericTest3()
    {
        Assert.AreEqual("l:*,a:**,s:**,v:*,e:*,g:*", Kata.GetStrings("Las Vegas"));
    }
}