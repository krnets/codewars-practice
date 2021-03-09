/*namespace smile67Kata
{
    using System.Numerics;

    public class Kata
    {
        public int nextHigher(int value)
        {
            var countBits = BitOperations.PopCount((uint) value);
            int nextValue = value + 1;
            var nextValueBits = BitOperations.PopCount((uint) nextValue);

            while (countBits != nextValueBits)
            {
                nextValue++;
                nextValueBits = BitOperations.PopCount((uint) nextValue);
            }

            return nextValue;
        }
    }
}*/

namespace smile67Kata
{
    using System.Numerics;

    public class Kata
    {
        public int nextHigher(int value)
        {
            var popCountOriginal = BitOperations.PopCount((uint) value);

            do
            {
                value++;
            } while (popCountOriginal != BitOperations.PopCount((uint) value));

            return value;
        }
    }
}