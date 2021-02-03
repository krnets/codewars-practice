using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        var expected = string.Join(",",
            new string[] {"EURGBP", "EURAUD", "EURNZD", "EURUSD", "EURCAD", "EURCHF", "EURJPY"});
        Assert.AreEqual(expected, string.Join(",", Kata.GenerateCurrencyMatrix("EUR")));

        expected = string.Join(",",
            new string[] {"EURGBP", "GBPAUD", "GBPNZD", "GBPUSD", "GBPCAD", "GBPCHF", "GBPJPY"});
        Assert.AreEqual(expected, string.Join(",", Kata.GenerateCurrencyMatrix("GBP")));

        expected = string.Join(",",
            new string[] {"EURCHF", "GBPCHF", "AUDCHF", "NZDCHF", "USDCHF", "CADCHF", "CHFJPY"});
        Assert.AreEqual(expected, string.Join(",", Kata.GenerateCurrencyMatrix("CHF")));
    }
}