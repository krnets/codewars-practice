using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!", Kata.Gordon("What feck damn cake"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("@R*!!!! Y**!!!! ST*!!!! P*D!!!!", Kata.Gordon("are you stu pid"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("*!!!! @M!!!! @!!!! CH*F!!!!", Kata.Gordon("i am a chef"));
    }
}