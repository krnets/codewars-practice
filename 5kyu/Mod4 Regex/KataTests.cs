using NUnit.Framework;

public class Mod4Test
{
    [Test]
    public void TestValidMod4()
    {
        string[] validTests =
        {
            "[+05620]", "[005624]", "[-05628]", "[005632]", "[555636]", "[+05640]",
            "[005600]", "the beginning [-0] the end", "~[4]", "[32]",
            "the beginning [0] ... [invalid] numb[3]rs ... the end", "...may be [+002016] will be."
        };
        foreach (var test in validTests)
        {
            Assert.IsTrue(Mod.MOD4.IsMatch(test), test + " is valid, but no match was made.");
        }
    }

    [Test]
    public void TestInvalidMod4()
    {
        string[] invalidTests =
            {"[+05621]", "[-55622]", "[005623]", "[~24]", "[8.04]", "No, [2014] isn't a multiple of 4..."};
        foreach (var test in invalidTests)
        {
            Assert.IsFalse(Mod.MOD4.IsMatch(test), test + " is invalid, but a match was made.");
        }
    }
}