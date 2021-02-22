using System.Linq;

namespace myjinxin
{
    public class Kata
    {
        public int HouseNumbersSum(int[] inputArray)
        {
            return inputArray.TakeWhile(x => x != 0).Sum();
        }
    }
}