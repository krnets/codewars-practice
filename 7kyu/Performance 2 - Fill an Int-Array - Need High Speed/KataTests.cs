using System;
using NUnit.Framework;

[TestFixture]
public class PerformanceTests
{  
    private Random rand = new Random((int)DateTime.Now.Ticks);
      
    [Test]
    public void PerformanceTest()
    {    
        var actual = Kata.Performance();
    
        Assert.AreEqual(4000000, actual.Length, "Wrong length of the array!");
        Assert.AreEqual(0, actual[0], "The content of the array is not correct.");
        Assert.AreEqual(3999999, actual[3999999], "The content of the array is not correct.");
    
        for(int i=0; i<10; i++)
        {
            int position = rand.Next(0, 3999999);
            Assert.AreEqual(position, actual[position], "The content of the array is not correct.");
        }
    }  
}