using NUnit.Framework;
using System;

[TestFixture]
public class Currying
{
    [Test, Description("must return an array")]
    public void ArrayTest()
    {
        Assert.IsTrue(Kata.MultiplyAll(new int[] {1})(1).GetType().IsArray);
    }

    [Test, Description("array has correct length")]
    public void LengthTest()
    {
        Assert.IsTrue(Kata.MultiplyAll(new int[] {1, 2})(1).Length == 2);
    }

    [Test, Description("returned array has correct values")]
    public void ValuesTest()
    {
        Assert.AreEqual(Kata.MultiplyAll(new int[] {1, 2, 3})(1), new int[] {1, 2, 3});
        Assert.AreEqual(Kata.MultiplyAll(new int[] {1, 2, 3})(2), new int[] {2, 4, 6});
        Assert.AreEqual(Kata.MultiplyAll(new int[] {1, 2, 3})(0), new int[] {0, 0, 0});
        Assert.AreEqual(Kata.MultiplyAll(new int[] { })(10), new int[] { }, "should return an empty array");
    }
}