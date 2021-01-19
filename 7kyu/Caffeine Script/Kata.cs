public class Kata
{
    public static string CaffeineBuzz(int n)
    {
        return n % 3 == 0 ? (n % 4 == 0 ? "Coffee" : "Java") + (n % 2 == 0 ? "Script" : "") : "mocha_missing!";
    }
}