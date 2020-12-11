public class Kata
{
    public static int CalculateYears(double principal, double interest, double tax, double desiredPrincipal)
    {
        int years = 0;
        double growth, taxed;

        while (principal < desiredPrincipal)
        {
            growth = principal * (1 + interest) - principal;
            taxed = growth * tax;
            principal += growth - taxed;

            years++;
        }

        return years;
    }
}