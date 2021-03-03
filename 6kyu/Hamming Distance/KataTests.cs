using NUnit.Framework;

[TestFixture]
public class HammingTests
{
	[TestCase("hello world", "hello world", 0)]
	[TestCase("I like turtles", "I like turkeys", 3)]
	public void StaticTests(string a, string b, int expected)
	{
		Assert.AreEqual(expected, Hamming.Distance(a, b), 
        string.Format("Expected hamming distance of '{0}' and '{1}' to be {2}", a, b, expected));
	}
}