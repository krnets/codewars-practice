namespace Kata
{
    using NUnit.Framework;

    [TestFixture]
    public class RockPaperScissorsLizardSpockTests
    {
        [TestCase("Rock", "Lizard")]
        [TestCase("rock", "scissor")]
        [TestCase("rock", "lizard")]
        [TestCase("lizard", "paper")]
        [TestCase("lizard", "spock")]
        [TestCase("Lizard", "Spock")]
        [TestCase("spock", "scissor")]
        [TestCase("spock", "rock")]
        [TestCase("scissor", "paper")]
        [TestCase("scissor", "lizard")]
        [TestCase("paper", "rock")]
        [TestCase("paper", "spock")]
        public void TestPlayer1Won(string p1, string p2)
        {
            Assert.AreEqual("Player 1 won!", Kata.RPSLP(p1, p2));
        }

        [TestCase("rock", "scissor")]
        [TestCase("rock", "lizard")]
        [TestCase("Rock", "Lizard")]
        [TestCase("lizard", "paper")]
        [TestCase("lizard", "spock")]
        [TestCase("spock", "scissor")]
        [TestCase("spock", "rock")]
        [TestCase("Spock", "Rock")]
        [TestCase("scissor", "paper")]
        [TestCase("scissor", "lizard")]
        [TestCase("paper", "rock")]
        [TestCase("paper", "spock")]
        [TestCase("Paper", "Rock")]
        public void TestPlayer2Won(string p1, string p2)
        {
            // twisted Parameter !!
            Assert.AreEqual("Player 2 won!", Kata.RPSLP(p2, p1));
        }

        [TestCase("rock")]
        [TestCase("lizard")]
        [TestCase("spock")]
        [TestCase("scissor")]
        [TestCase("paper")]
        public void TestDrawGame(string p1)
        {
            Assert.AreEqual("Draw!", Kata.RPSLP(p1, p1));
        }

        [TestCase("foo", "boo")]
        [TestCase("foo", "")]
        [TestCase("", "")]
        [TestCase(null, "")]
        [TestCase("", null)]
        [TestCase(null, null)]
        public void TestUnknownParameter(string p1, string p2)
        {
            Assert.AreEqual("Oh, Unknown Thing", Kata.RPSLP(p1, p2));
        }
    }
}