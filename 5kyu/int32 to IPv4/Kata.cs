/*using System;
using System.Linq;

public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        var binary = Convert.ToString(ip, 2).PadLeft(32, '0');

        return string.Join(".", Enumerable.Range(0, 4).Select(i => Convert.ToInt32(binary.Substring(i * 8, 8), 2)));
    }
}*/

/*public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        return (ip >> 24) % 256 + "." +
               (ip >> 16) % 256 + "." +
               (ip >> 8) % 256 + "." +
               ip % 256;
    }
}*/

/*public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        return (ip >> 24 & 0xFF) + "." +
               (ip >> 16 & 0xFF) + "." +
               (ip >> 8 & 0xFF) + "." +
               (ip & 0xFF);
    }
}*/

/*using System.Linq;
using System.Net;

public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        return string.Join(".", new IPAddress(ip).ToString().Split(".").Reverse());
    }
}*/

/*
using System.Linq;

public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        return string.Join(".", (new[] {24, 16, 8, 0}).Select(v => ip >> v & 0xFF));
    }
}
*/

using System;
using System.Linq;
using System.Net;

public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        var bytes = BitConverter.GetBytes(ip).Reverse().ToArray();

        return new IPAddress(bytes).ToString();
    }
}