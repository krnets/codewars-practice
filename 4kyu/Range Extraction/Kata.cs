using System.Text;

public class RangeExtraction
{
    public static string Extract(int[] args)
    {
        var sb = new StringBuilder();

        for (int i = 0; i < args.Length; i++)
        {
            sb.Append(args[i]);

            {
                int rangeEnd = i;

                while ((rangeEnd < args.Length - 1) && (args[rangeEnd + 1] - args[rangeEnd] == 1))
                    rangeEnd++;

                if (rangeEnd > (i + 1))
                {
                    sb.Append("-").Append(args[rangeEnd]);
                    i = rangeEnd;
                }
            }

            sb.Append(",");
        }

        return $"{sb}"[..^1];
    }
}