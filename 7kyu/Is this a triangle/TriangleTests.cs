using NUnit.Framework;

namespace Kata
{
    [TestFixture]
    public class TriangleTests
    {
        [Test]
        public void IsTriangle_ValidPostiveNumbers_ReturnsTrue()
        {
            Assert.IsTrue(Triangle.IsTriangle(5, 7, 10));
        }
    }
}