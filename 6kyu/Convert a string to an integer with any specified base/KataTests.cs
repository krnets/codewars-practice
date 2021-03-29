using NUnit.Framework;
using System;
using System.Collections.Generic;

[TestFixture]
public class BasicTest
{
    public static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new object[] {"10", 2}).Returns(2);
            yield return new TestCaseData(new object[] {"10", 3}).Returns(3);
            yield return new TestCaseData(new object[] {"12", 4}).Returns(6);
            yield return new TestCaseData(new object[] {"1234567890", 10}).Returns(1234567890);
            yield return new TestCaseData(new object[] {"FF", 16}).Returns(255);
            yield return new TestCaseData(new object[] {"FF", 18}).Returns(285);
            yield return new TestCaseData(new object[] {"ff", 18}).Returns(285);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int Test(string value, int fromBase) =>
        value.Parse(fromBase);
}

[TestFixture]
public class NegativeTest
{
    public static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(new object[] {"80000000", 16}).Returns(Int32.MinValue);
            yield return new TestCaseData(new object[] {"FFFFFFFF", 16}).Returns(-1);
            yield return new TestCaseData(new object[] {"1A20DCD80", 15}).Returns(-1);
            yield return new TestCaseData(new object[] {"1904440553", 11}).Returns(-1);
            yield return new TestCaseData(new object[] {"1550104015503", 6}).Returns(-1);
            yield return new TestCaseData(new object[] {"10000000" + "00000000" + "00000000" + "00000000", 2})
                .Returns(Int32.MinValue);
            yield return new TestCaseData(new object[] {"11111111" + "11111111" + "11111111" + "11111111", 2})
                .Returns(-1);
            yield return new TestCaseData(new object[] {"11111111" + "11111111" + "11111111" + "00000000", 2})
                .Returns(-256);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int Test(string value, int fromBase) =>
        value.Parse(fromBase);
}

[TestFixture]
public class ExceptionTest
{
    [Test]
    public void Test()
    {
        Assert.That(() => "FFFFFFFFFF".Parse(16), Throws.TypeOf<OverflowException>());
        Assert.That(() => "FFFFFFFF".Parse(15), Throws.TypeOf<FormatException>());
        Assert.That(() => "".Parse(15), Throws.TypeOf<ArgumentException>());
        string str = null;
        Assert.That(() => str.Parse(15), Throws.TypeOf<ArgumentNullException>());
        Assert.That(() => "0".Parse(1), Throws.TypeOf<ArgumentException>());
        Assert.That(() => "0".Parse(37), Throws.TypeOf<ArgumentException>());
    }
}