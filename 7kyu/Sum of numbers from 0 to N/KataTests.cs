using NUnit.Framework;

namespace Solution
{
    [TestFixture]
    public class SequenceSumTests
    {
        [Test]
        public void Sum()
        {
            Assert.AreEqual("0+1+2+3+4+5+6 = 21", SequenceSum.ShowSequence(6));
        }
        [Test]
        public void Negative()
        {
            Assert.AreEqual("-15<0", SequenceSum.ShowSequence(-15));
        }
        [Test]
        public void Zero()
        {
            Assert.AreEqual("0=0", SequenceSum.ShowSequence(0));
        }
    }
}