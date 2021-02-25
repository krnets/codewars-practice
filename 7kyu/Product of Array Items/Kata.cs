namespace Kata
{
    using System;
    using System.Linq;

    public class ArrayMath
    {
        public static int Product(int[] values)
        {
            // if (values == null) throw new argumentnullexception();
            // if (values.length == 0) throw new invalidoperationexception();

            // return values.Aggregate(1, (x, y) => x * y);
            return values.Aggregate((x, y) => x * y);
        }
    }
}