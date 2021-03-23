using NUnit.Framework;

class ExampleTest
{
    [Test]
    public void FixedTest0()
    {
        Assert.AreEqual(0, Kata.SequenceClassifier(new[] {3, 5, 8, 1, 14, 3}));
    }

    [Test]
    public void FixedTest1()
    {
        Assert.AreEqual(1, Kata.SequenceClassifier(new[] {3, 5, 8, 9, 14, 23}));
        Assert.AreEqual(1, Kata.SequenceClassifier(new[] {8, 9}));
    }

    [Test]
    public void FixedTest2()
    {
        Assert.AreEqual(2, Kata.SequenceClassifier(new[] {3, 5, 8, 8, 14, 14}));
        Assert.AreEqual(2, Kata.SequenceClassifier(new[] {8, 8, 8, 8, 8, 9}));
    }

    [Test]
    public void FixedTest3()
    {
        Assert.AreEqual(3, Kata.SequenceClassifier(new[] {14, 9, 8, 5, 3, 1}));
        Assert.AreEqual(3, Kata.SequenceClassifier(new[] {9, 8}));
    }

    [Test]
    public void FixedTest4()
    {
        Assert.AreEqual(4, Kata.SequenceClassifier(new[] {14, 14, 8, 8, 5, 3}));
        Assert.AreEqual(4, Kata.SequenceClassifier(new[] {9, 9, 9, 8, 8, 8}));
    }

    [Test]
    public void FixedTest5()
    {
        Assert.AreEqual(5, Kata.SequenceClassifier(new[] {8, 8, 8, 8, 8, 8}));
    }
}