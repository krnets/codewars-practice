using System.Linq;

namespace Kata
{
    public static class Kata
    {
        public static int[] UpArray(int[] num)
        {
            if (num.Length == 0 || num.Any(x => x < 0 || x > 9))
                return null;

            for (int i = num.Length - 1; i >= 0; i--)
            {
                if (num[i] < 9)
                {
                    num[i]++;
                    return num;
                }

                num[i] = 0;
            }

            return new[] {1}.Concat(new int[num.Length]).ToArray();
        }
    }
}