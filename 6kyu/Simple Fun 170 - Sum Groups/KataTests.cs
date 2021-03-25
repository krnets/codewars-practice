using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTests()
    {
        var kata = new Kata();

        Assert.AreEqual(6, kata.SumGroups(new int[] {2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9}));

        Assert.AreEqual(5, kata.SumGroups(new int[] {2, 1, 2, 2, 6, 5, 0, 2, 0, 3, 3, 3, 9, 2}));

        Assert.AreEqual(1, kata.SumGroups(new int[] {1}));

        Assert.AreEqual(1, kata.SumGroups(new int[] {2}));

        Assert.AreEqual(2, kata.SumGroups(new int[] {1, 2}));

        Assert.AreEqual(1, kata.SumGroups(new int[] {1, 1, 2, 2}));
    }
}