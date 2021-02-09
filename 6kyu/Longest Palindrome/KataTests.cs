﻿namespace Solution {
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [TestCase("", ExpectedResult = 0, Description = "empty string test")]
        [TestCase(null, ExpectedResult = 0, Description = "'null' value test")]
        [TestCase("a", ExpectedResult = 1, Description = "'a' value test")]
        [TestCase("aa", ExpectedResult = 2, Description = "'aa' value test")]
        [TestCase("baa", ExpectedResult = 2, Description = "'baa' value test")]
        [TestCase("abc0cba1", ExpectedResult = 7, Description = "'abc0cba1' value test")]
        [TestCase("12 21glg", ExpectedResult = 5, Description = "'12 21glg' value test")]
        [TestCase("   ", ExpectedResult = 3, Description = "empty space test")]
        [TestCase(@"\r\nn\r\", ExpectedResult = 8, Description = "secret test1")]
        [TestCase(@"|.\.\.|", ExpectedResult = 7, Description = "secret test2")]
        [TestCase("арозаупаланалапуазора", ExpectedResult = 21, Description = "russian secret test3")]
        [TestCase("WWiww", ExpectedResult = 2, Description = "secret test4")]
        public int SampleTest(string str)
        {
            return Kata.GetLongestPalindrome(str);
        }
    }
}