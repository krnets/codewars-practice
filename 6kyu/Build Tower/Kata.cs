/*using System.Linq;
using System.Text;

public class Kata
{
    public static string[] TowerBuilder(int nFloors)
    {
        string[] floors = new string[nFloors];

        for (int i = 1; i <= nFloors; i++)
        {
            var floor = new StringBuilder();
            floor.Append(string.Concat(Enumerable.Repeat(" ", nFloors - i)));
            floor.Append(string.Concat(Enumerable.Repeat("*", 2 * i - 1)));
            floor.Append(string.Concat(Enumerable.Repeat(" ", nFloors - i)));

            floors[i - 1] = floor.ToString();
        }

        return floors;
    }
}*/

public class Kata
{
    public static string[] TowerBuilder(int nFloors)
    {
        string[] floors = new string[nFloors];

        for (int i = 1; i <= nFloors; i++)
            floors[i - 1] = string.Concat(
                new string(' ', nFloors - i),
                new string('*', 2 * i - 1),
                new string(' ', nFloors - i)
            );

        return floors;
    }
}