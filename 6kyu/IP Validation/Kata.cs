/*
using System.Text.RegularExpressions;

namespace Solution
{
    class Kata
    {
        public static bool is_valid_IP(string ipAddres)
        {
            return Regex.IsMatch(ipAddres, @"^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$");
        }
    }
}
*/

using System.Net;

namespace Solution
{
    class Kata
    {
        public static bool is_valid_IP(string ipAddres)
        {
            IPAddress ip;
            var valid = IPAddress.TryParse(ipAddres, out ip);
            
            return valid && ip.ToString() == ipAddres;
        }
    }
}