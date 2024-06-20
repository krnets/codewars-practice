/*using System.Text.RegularExpressions;

namespace Solution
{
    class FileNameExtractor
    {
        public static string ExtractFileName(string dirtFileName)
        {
            return Regex.Replace(dirtFileName, @"^(\d+)_|.(\w+)$", "");
        }
    }
}*/

/*namespace Solution
{
    class FileNameExtractor
    {
        public static string ExtractFileName(string dirtFileName)
        {
            return dirtFileName[(dirtFileName.IndexOf('_') + 1)..dirtFileName.LastIndexOf('.')];
        }
    }
}*/

/*using System.Text.RegularExpressions;

namespace Solution
{
    class FileNameExtractor
    {
        public static string ExtractFileName(string dirtFileName)
        {
            return Regex.Split(dirtFileName, @"_(.*)\.")[1];
        }
    }
}*/

using System.Text.RegularExpressions;

namespace Solution
{
    class FileNameExtractor
    {
        public static string ExtractFileName(string dirtFileName)
        {
            return Regex.Match(dirtFileName, @"(?<=_).+(?=\.)").Value;
        }
    }
}