using System.Linq;

namespace Codewars
{
    public static class KataChallenge
    {
        public static bool IsDivisible(params int[] args)
        {
            return args.Skip(1).All(x => args[0] % x == 0);
        }
    }
}