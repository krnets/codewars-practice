using System.Linq;
using NUnit.Framework;

[TestFixture]
public class KataTest
{
    private Kata kata = new Kata();

    [Test]
    public void _0_Crossover_Basic_Tests()
    {
        Assert.AreEqual("111", kata.Crossover("110", "001", 2).ElementAt(0));
        Assert.AreEqual("000", kata.Crossover("110", "001", 2).ElementAt(1));

        Assert.AreEqual("111110", kata.Crossover("111000", "000110", 3).ElementAt(0));
        Assert.AreEqual("000000", kata.Crossover("111000", "000110", 3).ElementAt(1));
    }
}