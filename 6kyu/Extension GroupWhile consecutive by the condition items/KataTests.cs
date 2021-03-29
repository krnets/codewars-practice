using NUnit.Framework;
using System;
using System.Collections.Generic;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Func<object, bool> isLetter = (e) => char.IsLetter(Convert.ToChar(e));

        List<object> test = new List<object>
            {'L', 'e', 't', 't', 'e', 'r', '1', '2', '4', '=', 'a', 'B', 'E', 'l', 'T', '%'};

        var expected = new List<List<object>>
        {
            new List<object> {'L', 'e', 't', 't', 'e', 'r'},
            new List<object> {'1'},
            new List<object> {'2'},
            new List<object> {'4'},
            new List<object> {'='},
            new List<object> {'a', 'B', 'E', 'l', 'T'},
            new List<object> {'%'}
        };

        var actual = test.GroupWhile(isLetter);

        // Assert.AreEqual(expected, actual, $"Expected value: {expected.ToStringExt()}\nActual: {actual.ToStringExt()}");
        Assert.AreEqual(expected, actual, $"Expected value: {expected}\nActual: {actual}");
    }

    [Test]
    public void BasicTest2()
    {
        Func<object, bool> isGreaterThan10 = (e) => Convert.ToInt32(e) > 10;

        List<object> test = new List<object> {7, 8, 9, 10, 12, 14, 16, 18, 20};

        var expected = new List<List<object>>
        {
            new List<object> {7},
            new List<object> {8},
            new List<object> {9},
            new List<object> {10},
            new List<object> {12, 14, 16, 18, 20}
        };

        var actual = test.GroupWhile(isGreaterThan10);

        // Assert.AreEqual(expected, actual, $"Expected value: {expected.ToStringExt()}\nActual: {actual.ToStringExt()}");
        Assert.AreEqual(expected, actual, $"Expected value: {expected}\nActual: {actual}");
    }

    [Test]
    public void ExtendedTest1()
    {
        Func<object, bool> isGreaterThanOrEqual10AndEven = (e) =>
        {
            int element = Convert.ToInt32(e);

            return (element >= 10) && (element % 2 == 0);
        };

        List<object> test = new List<object> {7, 8, 9, 10, 10, 10, 12, 14, 16, 18, 20};

        var expected = new List<List<object>>
        {
            new List<object> {7},
            new List<object> {8},
            new List<object> {9},
            new List<object> {10, 10, 10, 12, 14, 16, 18, 20}
        };

        var actual = test.GroupWhile(isGreaterThanOrEqual10AndEven);

        Assert.AreEqual(expected, actual, $"Expected value: {expected}\nActual: {actual}");
    }

    [Test]
    public void ExtendedTest2()
    {
        Func<object, bool> isTrue = (e) => true;

        List<object> test = new List<object> {false, false, false, true, true, true, false, true};

        var expected = new List<List<object>>
        {
            new List<object> {false, false, false, true, true, true, false, true}
        };

        var actual = test.GroupWhile(isTrue);

        Assert.AreEqual(expected, actual, $"Expected value: {expected}\nActual: {actual}");
    }

    [Test]
    public void ExtendedTest3()
    {
        Func<object, bool> isString = (e) => e is string;

        List<object> test = new List<object> {"string", 19, new List<char> {'c'}, true, "that", "is", "string", null};

        var expected = new List<List<object>>
        {
            new List<object> {"string"},
            new List<object> {19},
            new List<object> {new List<char> {'c'}},
            new List<object> {true},
            new List<object> {"that", "is", "string"},
            new List<object> {null}
        };

        var actual = test.GroupWhile(isString);

        Assert.AreEqual(expected, actual, $"Expected value: {expected}\nActual: {actual}");
    }
}