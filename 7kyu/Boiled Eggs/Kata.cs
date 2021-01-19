/*public class Kata
{
    public static int CookingTime(int eggs)
    {
        int cookingTime = 5;
        int potCapacity = 8;

        return cookingTime * ((eggs + potCapacity - 1) / potCapacity);
    }
}*/
public class Kata
{
    public static int CookingTime(int eggs)
    {
        int eggBoilingTime = 5;
        int potCapacity = 8;
        int potsRequired = eggs / potCapacity;

        return eggBoilingTime * (eggs % 8 == 0 ? potsRequired : ++potsRequired);
    }
}