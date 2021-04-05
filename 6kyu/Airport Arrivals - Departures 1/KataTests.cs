using NUnit.Framework;
using System;

public class ExampleTests
{
    private string[] BEFORE(string[] a)
    {
        Console.WriteLine("Before:");
        return Preloaded.PrettyPrint(a);
    }

    private string[] AFTER(string[] a)
    {
        Console.WriteLine("After:");
        return Preloaded.PrettyPrint(a);
    }

    public void Example()
    {
        // CAT => DOG
        var before = BEFORE(new[] {"CAT"});
        var rotors = new int[][] {new[] {1, 13, 27}};
        var after = AFTER(Dinglemouse.FlapDisplay(before, rotors));
        var expected = new[] {"DOG"};
        Assert.AreEqual(expected, after);
    }

    [Test]
    public void Basic()
    {
        // HELLO => WORLD!
        var before = BEFORE(new[] {"HELLO "});
        var rotors = new int[][] {new[] {15, 49, 50, 48, 43, 13}};
        var after = AFTER(Dinglemouse.FlapDisplay(before, rotors));
        var expected = new[] {"WORLD!"};
        Assert.AreEqual(expected, after);

        // CODE => WARS
        var before2 = BEFORE(new[] {"CODE"});
        var rotors2 = new int[][] {new[] {20, 20, 28, 0}};
        var after2 = AFTER(Dinglemouse.FlapDisplay(before2, rotors2));
        var expected2 = new[] {"WARS"};
        Assert.AreEqual(expected2, after2);
    }
}