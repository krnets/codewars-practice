using NUnit.Framework;

[TestFixture]
public static class Opstrings1Tests
{
    private static void Testing(string actual, string expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        Testing(Opstrings1.Oper(Opstrings1.Rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"),
            "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif");
    }

    [Test]
    public static void Test2()
    {
        Testing(Opstrings1.Oper(Opstrings1.Rot, "rkKv\ncofM\nzXkh\nflCB"),
            "BClf\nhkXz\nMfoc\nvKkr");
    }

    [Test]
    public static void Test3()
    {
        Testing(Opstrings1.Oper(Opstrings1.SelfieAndRot, "xZBV\njsbS\nJcpN\nfVnP"),
            "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx");
    }

    [Test]
    public static void Test4()
    {
        Testing(Opstrings1.Oper(Opstrings1.SelfieAndRot, "uLcq\nJkuL\nYirX\nnwMB"),
            "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu");
    }
}