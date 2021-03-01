using NUnit.Framework;

[TestFixture]
public class KataTest
{
    private Kata kata = new Kata();

    [Test]
    public void _0_Generate_Should_Respect_Given_Length()
    {
        Assert.AreEqual(16, kata.Generate(16).Length);
        Assert.AreEqual(32, kata.Generate(32).Length);
        Assert.AreEqual(64, kata.Generate(64).Length);
    }
}