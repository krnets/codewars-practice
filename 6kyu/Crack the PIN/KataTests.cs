using NUnit.Framework;

[TestFixture]
public class Should_pass_all_of_these
{
    [Test]
    public void SimpleTest()
    {
        Assert.AreEqual("12345", CodeWars.crack("827ccb0eea8a706c4c34a16891f84e7b"));
    }
    [Test]
    public void HarderTest()
    {
        Assert.AreEqual("00078", CodeWars.crack("86aa400b65433b608a9db30070ec60cd"));
    }
}