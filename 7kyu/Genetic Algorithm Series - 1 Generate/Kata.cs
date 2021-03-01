using System;
using System.Linq;

public class Kata
{
    public string Generate(int length)
    {
        var rnd = new Random();

        return string.Concat(Enumerable.Range(0, length).Select(_ => rnd.Next(2)));
        // return string.Concat(new int[length].Select(_ => rnd.Next(2)));
    }
}