using NUnit.Framework;

[TestFixture]
public static class ScrambliesTests
{
    private static void Testing(bool actual, bool expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Testing(Scramblies.Scramble("rkqodlw", "world"), true);
        Testing(Scramblies.Scramble("cedewaraaossoqqyt", "codewars"), true);
        Testing(Scramblies.Scramble("katas", "steak"), false);
        Testing(Scramblies.Scramble("scriptjavx", "javascript"), false);
        Testing(Scramblies.Scramble("scriptingjava", "javascript"), true);
        Testing(Scramblies.Scramble("scriptsjava", "javascripts"), true);
        Testing(Scramblies.Scramble("javscripts", "javascript"), false);
        Testing(Scramblies.Scramble("aabbcamaomsccdd", "commas"), true);
        Testing(Scramblies.Scramble("commas", "commas"), true);
        Testing(Scramblies.Scramble("sammoc", "commas"), true);
    }
}