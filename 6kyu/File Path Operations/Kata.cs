/*class FileMaster
{
    private string _filePath, _fileName, _extension;

    public FileMaster(string filepath)
    {
        int i = filepath.LastIndexOf("/") + 1;
        int j = filepath.LastIndexOf(".") + 1;

        _filePath = filepath[..i];
        _fileName = filepath[i..(j - 1)];
        _extension = filepath[j..];
    }

    public string extension() => _extension;

    public string filename() => _fileName;

    public string dirpath() => _filePath;
}*/

using System.Text.RegularExpressions;
using static System.Reflection.MethodBase;

class FileMaster
{
    private Match regex;

    public FileMaster(string filepath) =>
        regex = Regex.Match(filepath, @"^(?<dirpath>[\s\S]+\/)(?<filename>\w+).(?<extension>\w+)$");

    public string extension() => regex.Groups[GetCurrentMethod().Name].Value;
    public string filename() => regex.Groups[GetCurrentMethod().Name].Value;
    public string dirpath() => regex.Groups[GetCurrentMethod().Name].Value;
}