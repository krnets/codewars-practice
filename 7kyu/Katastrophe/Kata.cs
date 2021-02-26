using System;
using System.Linq;

public class Kata
{
    public static string StrongEnough(int[][] earthquake, int age)
    {
        var damage = earthquake.Aggregate(1, (product, arr) => product * arr.Sum());
        var strength = 1000 * Math.Pow(0.99, age);

        return damage < strength ? "Safe!" : "Needs Reinforcement!";
    }
}