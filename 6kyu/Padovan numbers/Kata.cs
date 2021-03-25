/*public class Padovan
{
    public long Get(int number)
    {
        return number < 3 ? 1 : Get(number - 2) + Get(number - 3);
    }
}*/

public class Padovan
{
    public long Get(int number)
    {
        long a = 1, b = 1, c = 1, d = 1;

        for (int i = 2; i < number; i++)
        {
            d = a + b;

            (a, b, c) = (b, c, d);
        }

        return d;
    }
}