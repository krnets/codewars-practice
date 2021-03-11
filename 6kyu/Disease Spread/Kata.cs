using System.Collections.Generic;
using System.Linq;

class Epidem
{
    public static int Epidemic(int tm, int n, int s0, int i0, double b, double a)
    {
        var dt = (double) tm / n;
        var suspect = new List<double> {s0};
        var infect = new List<double> {i0};
        var recover = new List<double> {0};

        for (int i = 0; i < tm; i++)
        {
            for (int j = 1; j < n + 1;)
            {
                suspect.Add((suspect[j - 1] - dt * b * suspect[j - 1] * infect[j - 1]));
                infect.Add((infect[j - 1] + dt * (b * suspect[j - 1] * infect[j - 1] - a * infect[j - 1])));
                recover.Add((recover[j - 1] + dt * infect[j - 1] * a));

                if (infect[j] > 0) j++;
                else break;
            }
        }

        return (int) infect.Max();
    }
}