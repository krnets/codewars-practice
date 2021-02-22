using System;

public static class Kata
{
    public static string AddBinary(int a, int b)
    {
        return Convert.ToString(a + b, 2);
    }
}

/*using System.Text;

public static class Kata
{
    public static string AddBinary(int a, int b)
    {
        var sb = new StringBuilder();
        int sum = a + b;

        while (sum > 0)
        {
            sb.Insert(0, sum % 2);
            sum /= 2;
        }

        return sb.ToString();
    }
}*/