using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExamplesPositive()
    {
        Assert.AreEqual("This is a test!", Kata.VowelShift("This is a test!", 0));
        Assert.AreEqual("Thes is i tast!", Kata.VowelShift("This is a test!", 1));
        // Assert.AreEqual("Thes is i tast!", Kata.VowelShift("iiae
        // Assert.AreEqual("                                  eiia
        Assert.AreEqual("This as e tist!", Kata.VowelShift("This is a test!", 3));
        // Assert.AreEqual("This as e tist!", Kata.VowelShift("iiae
        // Assert.AreEqual(                                "iaei

        Assert.AreEqual("This is a test!", Kata.VowelShift("This is a test!", 4));
    }

    [Test]
    public void ExamplesNegative()
    {
        Assert.AreEqual("This as e tist!", Kata.VowelShift("This is a test!", -1));
        // Assert.AreEqual("This as e tist!", Kata.VowelShift("iiae
        // Assert.AreEqual("                                    iaei
        Assert.AreEqual("This as e tist!", Kata.VowelShift("This is a test!", -5));
    }
}