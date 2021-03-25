using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("kaka", Kata.KaCokadekaMe("ka"));
        Assert.AreEqual("kaa", Kata.KaCokadekaMe("a"));
        Assert.AreEqual("kaaa", Kata.KaCokadekaMe("aa"));
        Assert.AreEqual("kaz", Kata.KaCokadekaMe("z"));
        Assert.AreEqual("kaAkabbaa", Kata.KaCokadekaMe("Abbaa"));
        Assert.AreEqual("kamaikantekanakance", Kata.KaCokadekaMe("maintenance"));
        Assert.AreEqual("kaWookadie", Kata.KaCokadekaMe("Woodie"));
        Assert.AreEqual("kaIkancokamprekahekansikabikalikatiekas", Kata.KaCokadekaMe("Incomprehensibilities"));
    }
}