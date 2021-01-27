using NUnit.Framework;
[TestFixture]
class Tests
{
    [TestCase("n", "Woohoo!")]
    [TestCase("_nnnnnnn_n__n______nn__nn_nnn", "Car Dead")]
    [TestCase("______n___n_", "Woohoo!")]
    public void BasicTests(string input, string expected)
    {
        Assert.That(Kata.Bump(input), Is.EqualTo(expected));
    }
}