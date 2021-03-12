using NUnit.Framework;
using System;

[TestFixture]
public class CheckerboardTest
{
    [Test, Description("Should pass provided sample tests")]
    public void SampleTest()
    {
        Assert.AreEqual(String.Empty, Kata.Checkerboard(0));
        Assert.AreEqual("[r][b][r][b][r]\n" +
                        "[b][r][b][r][b]\n" +
                        "[r][b][r][b][r]\n" +
                        "[b][r][b][r][b]\n" +
                        "[r][b][r][b][r]\n", Kata.Checkerboard(5));
        Assert.AreEqual("[r][b][r][b][r][b][r][b]\n" +
                        "[b][r][b][r][b][r][b][r]\n" +
                        "[r][b][r][b][r][b][r][b]\n" +
                        "[b][r][b][r][b][r][b][r]\n" +
                        "[r][b][r][b][r][b][r][b]\n" +
                        "[b][r][b][r][b][r][b][r]\n" +
                        "[r][b][r][b][r][b][r][b]\n" +
                        "[b][r][b][r][b][r][b][r]\n", Kata.Checkerboard(8));
    }
}