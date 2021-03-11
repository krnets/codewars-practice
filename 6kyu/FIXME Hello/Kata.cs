using System.Collections.Generic;
using System.Linq;

public class Dinglemouse
{
    private readonly Dictionary<string, string> map = new Dictionary<string, string>();

    public Dinglemouse SetAge(int age)
    {
        var s = $"I am {age}.";

        if (!map.ContainsValue(s))
            map["age"] = s;

        return this;
    }

    public Dinglemouse SetSex(char sex)
    {
        var s = $"I am {(sex == 'M' ? "male" : "female")}.";

        if (!map.ContainsValue(s))
            map["sex"] = s;

        return this;
    }

    public Dinglemouse SetName(string name)
    {
        var s = $"My name is {name}.";

        if (!map.ContainsValue(s))
            map["name"] = s;

        return this;
    }

    public string Hello()
    {
        return map.Aggregate("Hello.", (acc, pair) => $"{acc} {pair.Value}");
    }
}