using NUnit.Framework;
using System;
public class Examples
{
    [Test]
    public void Example()
    {
        var expected =
            "6|██ 5%\n" +
            "5|\n" +
            "4|███████ 15%\n" +
            "3|███████████████████████████████████ 70%\n" +
            "2|█ 3%\n" +
            "1|███ 7%\n";
        Assert.AreEqual(expected, 
            Dinglemouse.Histogram(new int[] { 7, 3, 70, 15, 0, 5 }));
    }
}