using System.Linq;

public class solution
{
    public bool validate(string n)
    {
        return n.Reverse()
            .Where(char.IsDigit)
            .Select(c => (int) char.GetNumericValue(c))
            .Select((v, i) => i % 2 == 0 ? v : 2 * v)
            .Select(v => v > 9 ? v - 9 : v)
            .Sum() % 10 == 0;
    }
}