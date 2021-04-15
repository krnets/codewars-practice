using NUnit.Framework;

public class StripCommentsTest
{
    [Test]
    public void StripComments1()
    {
        Assert.AreEqual(
            "apples, pears\ngrapes\nbananas",
            StripCommentsSolution.StripComments("apples, pears # and bananas\ngrapes\nbananas !apples",
                new string[] {"#", "!"}));
    }

    [Test]
    public void StripComments2()
    {
        Assert.AreEqual("a\nc\nd", StripCommentsSolution.StripComments("a #b\nc\nd $e f g", new string[] {"#", "$"}));
    }

    [Test]
    public void EdgeCases()
    {
        Assert.AreEqual("a\n b\nc", StripCommentsSolution.StripComments("a \n b \nc ", new string[] {"#", "$"}));
        Assert.AreEqual("a", StripCommentsSolution.StripComments("a", new string[] {"1"}));
        Assert.AreEqual("", StripCommentsSolution.StripComments("a", new string[] {"a"}));
        Assert.AreEqual("", StripCommentsSolution.StripComments("            ", new string[] {"#"}));
        Assert.AreEqual("", StripCommentsSolution.StripComments("# some text", new string[] {"#"}));
    }
}