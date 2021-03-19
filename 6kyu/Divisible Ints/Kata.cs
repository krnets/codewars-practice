public class Kata
{
    public static int GetCount(int n)
    {
        var strNum = n.ToString();
        int count = 0;

        for (int i = 1; i < strNum.Length; i++)
        {
            for (int j = 0; j <= strNum.Length - i; j++)
            {
                var x = int.Parse(strNum[j..(i + j)]);

                if (x > 0 && n % x == 0)
                    count++;
            }
        }

        return count;
    }
}