using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(3,
            Kata.GetLengthOfMissingArray(new object[][]
                {new object[] {1, 2}, new object[] {4, 5, 1, 1}, new object[] {1}, new object[] {5, 6, 7, 8, 9}}));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(2,
            Kata.GetLengthOfMissingArray(new object[][]
                {new object[] {5, 2, 9}, new object[] {4, 5, 1, 1}, new object[] {1}, new object[] {5, 6, 7, 8, 9}}));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(2,
            Kata.GetLengthOfMissingArray(new object[][] {new object[] {null}, new object[] {null, null, null}}));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual(5,
            Kata.GetLengthOfMissingArray(new object[][]
            {
                new object[] {'a', 'a', 'a'}, new object[] {'a', 'a'}, new object[] {'a', 'a', 'a', 'a'},
                new object[] {'a'}, new object[] {'a', 'a', 'a', 'a', 'a', 'a'}
            }));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual(0, Kata.GetLengthOfMissingArray(new object[][] { }));
    }
}