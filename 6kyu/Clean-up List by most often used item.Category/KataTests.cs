namespace CleanUp
{
    using NUnit.Framework;
    using System.Collections.Generic;

    [TestFixture]
    public class TestExample
    {
        [Test]
        public void ExampleTest()
        {
            List<AmazonItem> test = new List<AmazonItem>();

            for (int i = 0; i < 5; i++)
            {
                test.Add(new AmazonItem() {Category = "MainCategory"});
            }

            test.Add(new AmazonItem() {Category = "Phones"});
            test.Add(new AmazonItem() {Category = "Notebooks"});

            var checker = AmazonWorker.LeaveOnlyMainCategoryItems(test);

            Assert.AreEqual(checker.Count, 5);
        }
    }
}