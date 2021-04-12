/*using System;

public class Kata
{
    public static Func<char> MakeLooper(string str)
    {
        int index = 0;

        return () => str[index++ % str.Length];
    }
}*/

/*
using System;

public class Kata
{
    public static Func<char> MakeLooper(string str)
    {
        int i = 0;

        return () =>
        {
            i = i == str.Length ? 0 : i++;
            return str[i++];
        };
    }
}
*/

using System;

public class Kata
{
    public static Func<char> MakeLooper(string str)
    {
        var iter = str.GetEnumerator();

        return () =>
        {
            if (!iter.MoveNext())
            {
                iter.Reset();
                iter.MoveNext();
            }

            return iter.Current;
        };
    }
}