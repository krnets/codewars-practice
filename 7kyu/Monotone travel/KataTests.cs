namespace Solution 
{
    using NUnit.Framework;
    using System;
    using System.Linq;

    [TestFixture]
    public class SolutionTest
    {
        [Test, Description("should work on increasing lists")]
        public void IncreasingTest()
        {
            Assert.AreEqual(true, Kata.IsMonotone(Enumerable.Range(1, 10).ToArray()));
            Assert.AreEqual(true, Kata.IsMonotone(Enumerable.Range(4, 9).ToArray()));
        }
    
        [Test, Description("should work on constant lists")]
        public void ConstantTest()
        {
            Assert.AreEqual(true, Kata.IsMonotone(new int[] {5, 5, 5, 5, 5}));
        }
    
        [Test, Description("should work on an empty list")]
        public void EmptyTest()
        {
            Assert.AreEqual(true, Kata.IsMonotone(new int[] {}));
        }
    
        [Test, Description("should return false on a decreasing list")]
        public void DecreasingTest()
        {
            Assert.AreEqual(false, Kata.IsMonotone(Enumerable.Range(1, 5).Reverse().ToArray()));
        }
    
        [Test, Description("should work on a non-decreasing list")]
        public void NonDecreasingTest()
        {
            Assert.AreEqual(true, Kata.IsMonotone(new int[] {1, 2, 3, 3, 4, 5}));
        }
    }
}