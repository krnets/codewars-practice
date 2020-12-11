using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    [TestCase("foefet", "toffee", ExpectedResult = true)]
    [TestCase("Buckethead", "DeathCubeK", ExpectedResult = true)]
    [TestCase("Twoo", "Woot", ExpectedResult = true)]
    [TestCase("apple", "pale", ExpectedResult = false)]
    public static bool FixedTest(string test, string original)
    {
        return Kata.IsAnagram(test, original);
    }
}