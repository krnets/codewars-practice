using NUnit.Framework;
using System.Linq;

[TestFixture]
public class SortingTest
{
    [Test]
    public void SimpleTests()
    {
        var source = new[]
        {
            "http://www.google.en/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
        };

        var expected = new[]
        {
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.en/?x=jsdfkj",
        };
        var result = source.OrderByDomain();

        foreach (var r in result) 
            System.Console.WriteLine(r);

        Assert.True(expected.SequenceEqual(result));
    }
}