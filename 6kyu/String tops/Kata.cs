using System.Text;

public static class Kata
{
    public static string Tops(string msg)
    {
        var sb = new StringBuilder();
        int counter = 1, i = 0;

        while ((i + counter) < msg.Length)
        {
            if (counter % 2 != 0)
                sb.Insert(0, msg[i + counter]);

            i += counter;
            counter++;
        }


        return sb.ToString();
    }
}