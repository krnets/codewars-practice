using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(new int[] {1, 18, 3, 2}, Solution.solve("Codewars@codewars123.com"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(new int[] {7, 6, 3, 2}, Solution.solve("bgA5<1d-tOwUZTS8yQ"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(new int[] {9, 9, 6, 9}, Solution.solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(new int[] {15, 8, 6, 9}, Solution.solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"));
    }
}