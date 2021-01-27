using NUnit.Framework;

[TestFixture]
public class Test
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(28, Kata.CubeOdd(new int[] {1, 2, 3, 4}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(0, Kata.CubeOdd(new int[] {-3, -2, 2, 3}));
    }
}