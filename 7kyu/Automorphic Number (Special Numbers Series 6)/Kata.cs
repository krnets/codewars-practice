/*using System;

class Kata
{
    public static string Automorphic(int n)
    {
        int digitLength = (int) Math.Floor(Math.Log10(n) + 1);

        return (n * n) % (int) (Math.Pow(10, digitLength)) == n ? "Automorphic" : "Not!!";
    }
}*/

using System;

class Kata
{
    public static string Automorphic(int n)
    {
        var digitLength = Math.Floor(Math.Log10(n) + 1);

        return (n * n) % Math.Pow(10, digitLength) == n ? "Automorphic" : "Not!!";
    }
}
/*class Kata
{
    public static string Automorphic(int n)
    {

        return $"{n * n}".EndsWith($"{n}") ? "Automorphic" : "Not!!";
    }
}*/