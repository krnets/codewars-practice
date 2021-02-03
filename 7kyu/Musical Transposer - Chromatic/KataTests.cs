using NUnit.Framework;

[TestFixture]
class ExampleTests
{
    [Test, Description("Should return the same note.")]
    public void UnisonTests()
    {
        Assert.AreEqual("A", Harmonizer.Transpose("A", 0));
        Assert.AreEqual("C", Harmonizer.Transpose("C", 0));
        Assert.AreEqual("F#", Harmonizer.Transpose("F#", 0));
    }

    [Test, Description("Should return the same note.")]
    public void OctaveTests()
    {
        Assert.AreEqual("C#", Harmonizer.Transpose("C#", 12));
        Assert.AreEqual("E", Harmonizer.Transpose("E", 12));
        Assert.AreEqual("G#", Harmonizer.Transpose("G#", 12));
    }

    [Test, Description("Should return the same note.")]
    public void SubOctaveTests()
    {
        Assert.AreEqual("A#", Harmonizer.Transpose("A#", -12));
        Assert.AreEqual("D", Harmonizer.Transpose("D", -12));
        Assert.AreEqual("F", Harmonizer.Transpose("F", -12));
    }

    [Test, Description("Should return the transposition of the given note by the given number of semi-tones.")]
    public void RandomIntervals()
    {
        Assert.AreEqual("C#", Harmonizer.Transpose("A", 4));
        Assert.AreEqual("B", Harmonizer.Transpose("A", -10));
        Assert.AreEqual("F", Harmonizer.Transpose("A#", 7));
        Assert.AreEqual("A", Harmonizer.Transpose("A#", -1));
        Assert.AreEqual("G#", Harmonizer.Transpose("B", 9));
        Assert.AreEqual("F", Harmonizer.Transpose("B", -6));
        Assert.AreEqual("G#", Harmonizer.Transpose("C", 8));
        Assert.AreEqual("A", Harmonizer.Transpose("C", -3));
        Assert.AreEqual("F#", Harmonizer.Transpose("C#", 5));
        Assert.AreEqual("D", Harmonizer.Transpose("C#", -11));
        Assert.AreEqual("E", Harmonizer.Transpose("D", 2));
        Assert.AreEqual("G", Harmonizer.Transpose("D", -7));
        Assert.AreEqual("D", Harmonizer.Transpose("D#", 11));
        Assert.AreEqual("B", Harmonizer.Transpose("D#", -4));
        Assert.AreEqual("G", Harmonizer.Transpose("E", 3));
        Assert.AreEqual("G", Harmonizer.Transpose("E", -9));
        Assert.AreEqual("D#", Harmonizer.Transpose("F", 10));
        Assert.AreEqual("D#", Harmonizer.Transpose("F", -2));
        Assert.AreEqual("G", Harmonizer.Transpose("F#", 1));
        Assert.AreEqual("C#", Harmonizer.Transpose("F#", -5));
        Assert.AreEqual("C#", Harmonizer.Transpose("G", 6));
        Assert.AreEqual("B", Harmonizer.Transpose("G", -8));
        Assert.AreEqual("D#", Harmonizer.Transpose("G#", 7));
        Assert.AreEqual("E", Harmonizer.Transpose("G#", -4));
    }
}