using NUnit.Framework;

[TestFixture]
public class KataTest
{
    private Warrior ninja = new Warrior("Ninja");
    private Warrior samurai = new Warrior("Samurai");

    [Test]
    public void Tests()
    {
        samurai.Strike(ninja, 4);
        Assert.AreEqual(60, ninja.Health);
    }
}