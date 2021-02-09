namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void ExampleTest1()
        {
            Assert.AreEqual("FILE_NAME.EXTENSION",
                FileNameExtractor.ExtractFileName("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"));
        }

        [Test]
        public void ExampleTest2()
        {
            Assert.AreEqual("FILE_NAME.EXTENSION",
                FileNameExtractor.ExtractFileName("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"));
        }
    }
}