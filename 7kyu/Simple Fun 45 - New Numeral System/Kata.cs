using System.Linq;

namespace myjinxin
{
    public class Kata
    {
        public string[] NewNumeralSystem(char number)
        {
            return Enumerable.Range(0, (number - 'A') / 2 + 1)
                .Select(i => $"{(char) ('A' + i)} + {(char) (number - i)}")
                .ToArray();
        }
    }
}