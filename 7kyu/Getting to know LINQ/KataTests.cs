using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void SumOfArrayTest()
    {
        Assert.AreEqual(6, Kata.Sum(new [] {2, 3, 1}));
    }
 
    [Test]
    public void CountOccurencesOfCharacterTest()
    {
        Assert.AreEqual(2, Kata.CountChar(new [] {'A', 'B', 'C', 'A'}, 'A'));
    }
  
    [Test]
    public void CalculateSquaresTest()
    {
        Assert.AreEqual(new [] {1, 4, 9, 16, 25, 36}, Kata.CalculateSquares(1, 6));
    }
}