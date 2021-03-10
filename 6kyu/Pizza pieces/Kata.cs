public class Pizza
{
    public static int maxPizza(int cut)
    {
        // return cut < 0 ? -1 : (cut + 1) * cut / 2 + 1;
        return cut < 0 ? -1 : cut * (cut + 1) / 2 + 1;
    }
}