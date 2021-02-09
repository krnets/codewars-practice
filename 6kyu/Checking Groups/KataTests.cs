using NUnit.Framework;

[TestFixture]
public class GroupsTests
{
    [TestCase("()", true)]
    [TestCase("({})", true)]
    [TestCase("[[]()]", true)]
    [TestCase("[{()}]", true)]
    [TestCase("({", false)]
    [TestCase("{(})", false)]
    [TestCase("([]", false)]
    [TestCase("[])", false)]
    [TestCase("([]", false)]
    [TestCase("[])", false)]
    [TestCase("([]))", false)]
    [TestCase("{{))", false)]
    [TestCase("{}{", false)]
    [TestCase("{", false)]
    [TestCase("]", false)]
    [TestCase("{{{{{{{{{{{((((((([])))))))}}}}}}}}}}", false)]
    public void Tests(string input, bool expected)
    {
        Assert.AreEqual(expected, Groups.Check(input));
    }
}