using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest()
    {
        Assert.AreEqual("covfefe", Solution.Covfefe("coverage"));
        Assert.AreEqual("covfefe covfefe", Solution.Covfefe("coverage coverage"));
        Assert.AreEqual("nothing covfefe", Solution.Covfefe("nothing"));
        Assert.AreEqual("double space  covfefe", Solution.Covfefe("double space "));
        Assert.AreEqual("covfefe covfefe", Solution.Covfefe("covfefe"));
        Assert.AreEqual(" covfefe", Solution.Covfefe(""));
    }
}