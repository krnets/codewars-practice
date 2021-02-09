using System.Linq;

namespace Main
{
    public class Kata
    {
        public static int[] DataReverse(int[] data)
        {
            return Enumerable.Range(0, data.Length / 8)
                .Select(i => data[(8 * i)..(8 * i + 8)])
                .Reverse()
                .SelectMany(byteArray => byteArray)
                .ToArray();
        }
    }
}

/*using System.Linq;

namespace Main
{
    public class Kata
    {
        public static int[] DataReverse(int[] data)
        {
            return Enumerable.Range(0, data.Length / 8)
                .Select(i => data.Skip(i * 8).Take(8).ToArray())
                .Reverse()
                .SelectMany(byteArray => byteArray)
                .ToArray();
        }
    }
}*/