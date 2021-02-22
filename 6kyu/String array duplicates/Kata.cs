/*using System.Text;

public class Solution
{
    public static string[] dup(string[] arr)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            var sb = new StringBuilder();

            for (int j = 0; j < arr[i].Length; j++)
            {
                if (j == 0)
                    sb.Append(arr[i][j]);

                else if (!arr[i][j - 1].Equals(arr[i][j]))
                    sb.Append(arr[i][j]);
            }

            arr[i] = sb.ToString();
        }

        return arr;
    }
}*/

/*using System.Linq;
using System.Text.RegularExpressions;

public class Solution
{
    public static string[] dup(string[] arr)
    {
        return arr.Select(word => Regex.Replace(word, @"(\w)\1+", "$1")).ToArray();
    }
}*/

/*using System.Text;

public class Solution
{
    public static string[] dup(string[] arr)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            var sb = new StringBuilder();

            for (int j = 0; j < arr[i].Length; j++)
                if (j == 0 || !arr[i][j - 1].Equals(arr[i][j]))
                    sb.Append(arr[i][j]);

            arr[i] = sb.ToString();
        }

        return arr;
    }
}*/

using System.Linq;

public class Solution
{
    public static string[] dup(string[] arr)
    {
        return arr.Select(word => string.Concat(word
                .Where((c, i) => i == 0 || c != word[i - 1])))
            .ToArray();
    }
}