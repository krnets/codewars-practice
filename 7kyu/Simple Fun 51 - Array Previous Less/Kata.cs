namespace myjinxin
{
    using System.Linq;

    public class Kata
    {
        public int[] ArrayPreviousLess(int[] arr)
        {
            return arr.Select((el, i) =>
                    arr.Take(i)
                        .Where(x => x < el)
                        .DefaultIfEmpty(-1)
                        .Last())
                .ToArray();
        }
    }
}