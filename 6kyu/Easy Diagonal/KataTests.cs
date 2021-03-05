using NUnit.Framework;
using System.Numerics;

[TestFixture]
public class DiagonalTests {

    [Test]
    public void Test1() {
        Assert.AreEqual(new BigInteger(5985), Diagonal.diagonal(20, 3));
    }
    [Test]
    public void Test2() {
        Assert.AreEqual(new BigInteger(20349), Diagonal.diagonal(20, 4));
    }
    [Test]
    public void Test3() {
        Assert.AreEqual(new BigInteger(54264), Diagonal.diagonal(20, 5));
    }
}