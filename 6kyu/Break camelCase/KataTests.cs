namespace Solution 
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class Sample_Tests
    {
        private static IEnumerable<TestCaseData> testCases
        {
            get
            {
                yield return new TestCaseData("camelCasing").Returns("camel Casing");
                yield return new TestCaseData("camelCasingTest").Returns("camel Casing Test");
            }
        }
  
        [Test, TestCaseSource("testCases")]
        public string Test(string str) => Kata.BreakCamelCase(str);
    }
}