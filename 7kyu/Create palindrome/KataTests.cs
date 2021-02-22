using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(true, Solution.solve("abba"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(false, Solution.solve("abaazaba"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(true, Solution.solve("abccba"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(true, Solution.solve("adfa"));
    }

    [Test]
    public void ExampleTest5()
    {
        Assert.AreEqual(false, Solution.solve("ae"));
    }

    [Test]
    public void ExampleTest6()
    {
        Assert.AreEqual(true, Solution.solve("sq"));
    }

    [Test]
    public void ExampleTest7()
    {
        Assert.AreEqual(false, Solution.solve("abzy"));
    }

    [Test]
    public void ExampleTest8()
    {
        Assert.AreEqual(true,
            Solution.solve(
                "kxbkwgyydkcbtjcosgikfdyhuuprubpwthgflucpyylbofvqxkkvqthmdnywpaunfihvupbwpruwfybdmgeuocltdaidyyewmbzm"));
    }
}