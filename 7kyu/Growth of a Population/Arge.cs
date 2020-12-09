class Arge
{
    public static int NbYear(int p0, double percent, int aug, int p)
    {
        int countYears = 0;

        while (p0 < p)
        {
            p0 = (int) (p0 * (1 + percent / 100)) + aug;
            countYears++;
        }

        return countYears;
    }
}