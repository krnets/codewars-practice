/*using System.Linq;

namespace myjinxin
{
    public class Kata
    {
        public int CountNumber(double n, double x)
        {
            var list = Enumerable.Range(1, (int) n).ToList();

            var matrix = Enumerable.Range(1, (int) n)
                .Select(i => list.Select(j => i * j))
                .ToList();

            return matrix.SelectMany(t => t).Count(v => v == (int) x);
        }
    }
}*/

namespace myjinxin
{
    public class Kata
    {
        public int CountNumber(double n, double x)
        {
            {
                int count = 0, i = 1;

                while (i * i < x)
                {
                    if (x % i == 0 && n * i >= x)
                        count += (i <= n ? 1 : 0) + (x / i <= n ? 1 : 0);

                    i++;
                }

                return count + (i * i == x && i <= n ? 1 : 0);
            }
        }
    }
}