using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void _0_BasicTests()
    {
        Assert.AreEqual(0, "00:00:00".ToSeconds());
        Assert.AreEqual(3723, "01:02:03".ToSeconds());
        Assert.AreEqual(null, "01:02:60".ToSeconds());
        Assert.AreEqual(null, "01:60:03".ToSeconds());
        Assert.AreEqual(359999, "99:59:59".ToSeconds());
        Assert.AreEqual(null, "0:00:00".ToSeconds());
        Assert.AreEqual(null, "00:0:00".ToSeconds());
        Assert.AreEqual(null, "00:00:0".ToSeconds());
        Assert.AreEqual(null, "00:00:00\n0".ToSeconds());
        Assert.AreEqual(null, "00\n00:00:00".ToSeconds());
    }
}