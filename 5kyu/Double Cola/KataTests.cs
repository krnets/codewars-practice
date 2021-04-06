using NUnit.Framework;

[TestFixture]
public class ListTests
{
    [Test]
    public void Test1()
    {
        string[] names = new string[] {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};
        int n = 1;
        Assert.AreEqual("Sheldon", Line.WhoIsNext(names, n));
    }

    [Test]
    public void Test2()
    {
        string[] names = new string[] {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};
        int n = 6;
        Assert.AreEqual("Sheldon", Line.WhoIsNext(names, n));
    }
}