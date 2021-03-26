using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTest1()
    {
        var kata = new Kata();

        Assert.AreEqual(true,
            kata.PairOfShoes(new int[][] {new int[] {0, 21}, new int[] {1, 23}, new int[] {1, 21}, new int[] {0, 23}}));
    }

    [Test]
    public void BasicTest2()
    {
        var kata = new Kata();
        Assert.AreEqual(false,
            kata.PairOfShoes(new int[][] {new int[] {0, 21}, new int[] {1, 23}, new int[] {1, 21}, new int[] {1, 23}}));
    }

    [Test]
    public void BasicTest3()
    {
        var kata = new Kata();
        Assert.AreEqual(true,
            kata.PairOfShoes(new int[][]
            {
                new int[] {0, 23}, new int[] {1, 21}, new int[] {1, 23}, new int[] {0, 21}, new int[] {1, 22},
                new int[] {0, 22}
            }));
    }

    [Test]
    public void BasicTest4()
    {
        var kata = new Kata();
        Assert.AreEqual(true,
            kata.PairOfShoes(new int[][] {new int[] {0, 23}, new int[] {1, 21}, new int[] {1, 23}, new int[] {0, 21}}));
    }

    [Test]
    public void BasicTest5()
    {
        var kata = new Kata();
        Assert.AreEqual(false, kata.PairOfShoes(new int[][] {new int[] {0, 23}}));
    }

    [Test]
    public void BasicTest6()
    {
        var kata = new Kata();
        Assert.AreEqual(true, kata.PairOfShoes(new int[][] {new int[] {0, 23}, new int[] {1, 23}}));
    }

    [Test]
    public void BasicTest7()
    {
        var kata = new Kata();
        Assert.AreEqual(false, kata.PairOfShoes(new int[][] {new int[] {0, 23}, new int[] {1, 22}}));
    }
}