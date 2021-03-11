using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void BasicTest1()
    {
        string expected = "□□□■\n" +
                          "□□■■\n" +
                          "□■■■\n" +
                          "■■■■";

        string actual = Kata.Draw(new int[] {1, 2, 3, 4});

        Assert.AreEqual(expected, actual);
    }

    [Test]
    public void BasicTest2()
    {
        string expected = "□□■■□□\n" +
                          "□■■■■□\n" +
                          "■■■■■■";

        string actual = Kata.Draw(new int[] {1, 2, 3, 3, 2, 1});

        Assert.AreEqual(expected, actual);
    }

    [Test]
    public void BasicTest3()
    {
        string expected = "□□□□□□□□□□□□■\n" +
                          "□□□□□□□□□□□■■\n" +
                          "□□□□□□□□□□■■■\n" +
                          "□□□□□□□□□■■■■\n" +
                          "□□■■□□□□■■■■■\n" +
                          "□■■■■□□■■■■■■\n" +
                          "■■■■■■■■■■■■■";

        string actual = Kata.Draw(new int[] {1, 2, 3, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7});

        Assert.AreEqual(expected, actual);
    }

    [Test]
    public void BasicTest4()
    {
        string expected = "□□□□□■□□□□□□□\n" +
                          "■□□□□■■□□□■□□\n" +
                          "■□□□■■■■□□■□□\n" +
                          "■■□□■■■■□■■□□\n" +
                          "■■□■■■■■■■■■□\n" +
                          "■■■■■■■■■■■■■";

        string actual = Kata.Draw(new int[] {5, 3, 1, 2, 4, 6, 5, 4, 2, 3, 5, 2, 1});

        Assert.AreEqual(expected, actual);
    }
}