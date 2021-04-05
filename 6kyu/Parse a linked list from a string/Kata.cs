using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static Node Parse(string nodes)
    {
        return Regex.Split(nodes, " -> ")
                    .SkipLast(1)
                    .Reverse()
                    .Aggregate<string, Node>(null, (current, strNum) => 
                        new Node(int.Parse(strNum), current));
        }
}