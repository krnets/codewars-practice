using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void FixedTest()
    {
        List<int> lst = new int[] {1, 2, 3, 4}.ToList();
        List<int> lstCopy = lst.Copy();
        Assert.That(lstCopy, Is.EqualTo(lst), "Copy unsuccessful");

        lst[1] += 5;
        Assert.That(lstCopy, Is.Not.EqualTo(lst), "The list was not properly copied");
    }
}