/*using System.Data;

namespace SolveIt
{
    public class Kata
    {
        public static int result(string stringInput)
        {
            return (int) new DataTable().Compute(stringInput, null);
        }
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

namespace SolveIt
{
    public class Kata
    {
        public static int result(string stringInput)
        {
            return Regex.Split(stringInput.Replace(" ", ""), "(?=[-+])").Sum(int.Parse);
        }
    }
}