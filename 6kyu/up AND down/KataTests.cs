using System;
using NUnit.Framework;

[TestFixture]
public static class UpdownTests
{
    private static void testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Console.WriteLine("Arrange");
        testing(Updown.Arrange("who hit retaining The That a we taken"),
            "who RETAINING hit THAT a THE we TAKEN"); // 3
        testing(Updown.Arrange("on I came up were so grandmothers"),
            "i CAME on WERE up GRANDMOTHERS so"); // 4
        testing(Updown.Arrange("way the my wall them him"),
            "way THE my WALL him THEM"); // 1
        testing(Updown.Arrange("turn know great-aunts aunt look A to back"),
            "turn GREAT-AUNTS know AUNT a LOOK to BACK"); // 2
    }
}