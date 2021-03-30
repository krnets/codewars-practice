using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public class TitleSorterTests
{
    [Test]
    public void SampleBooksSortTest()
    {
        List<string> titlesToSort = new List<string>()
        {
            "A Petition to Magic",
            "Heritage of Deceit",
            "Stingers",
            "Billy's Zombie",
            "Heaven and Earth: Paranormal Flash Fiction",
            "Tales From Virdura",
        };
        List<string> sortedList = new TitleSorter().Sort(titlesToSort);
        Assert.AreEqual(titlesToSort.Count, sortedList.Count);
        Assert.AreEqual("Billy's Zombie", sortedList[0]);
        Assert.AreEqual("A Petition to Magic", sortedList[3]);
    }
}