using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class CoinTest
{
    [Test]
    public void test01()
    {
        Kata c = new Kata();

        Assert.AreEqual(new List<string>() {"H", "T"}, c.coin(1));
        Assert.AreEqual(new List<string>() {"HH", "HT", "TH", "TT"}, c.coin(2));
        Assert.AreEqual(new List<string>() {"HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"}, c.coin(3));
    }
}