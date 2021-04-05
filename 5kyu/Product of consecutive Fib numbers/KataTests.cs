using NUnit.Framework;

[TestFixture]
public class ProdFibTests
{
    [Test]
    public void Test1()
    {
        ulong[] r = new ulong[] {55, 89, 1};
        Assert.AreEqual(r, ProdFib.productFib(4895));
    }
}