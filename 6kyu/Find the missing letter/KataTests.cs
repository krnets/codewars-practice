using NUnit.Framework;

public class KataTests
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual('e', Kata.FindMissingLetter(new[] {'a', 'b', 'c', 'd', 'f'}));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual('P', Kata.FindMissingLetter(new[] {'O', 'Q', 'R', 'S'}));
    }
}