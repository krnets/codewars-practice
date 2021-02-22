using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(new String[] {"codewars", "picaniny", "hubububo"},
            Solution.dup(new String[] {"ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"}));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(new String[] {"abracadabra", "alote", "asese"},
            Solution.dup(new String[] {"abracadabra", "allottee", "assessee"}));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(new String[] {"keles", "kenes"}, Solution.dup(new String[] {"kelless", "keenness"}));
    }
}