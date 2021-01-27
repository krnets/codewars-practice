using System.Linq;

class Kata
{
    public static string StrongNumber(int number)
    {
        return number.ToString()
            .Select(c => (int) char.GetNumericValue(c))
            .Select(n => Enumerable.Range(1, n).Aggregate(1, (a, b) => a * b))
            .Sum() == number
            ? "STRONG!!!!"
            : "Not Strong !!";
    }
}