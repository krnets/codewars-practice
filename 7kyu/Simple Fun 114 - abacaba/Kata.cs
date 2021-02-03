namespace myjinxin
{
    public class Kata
    {
        private string str = "a";

        public Kata()
        {
            for (int i = 1; i < 26; i++)
                str = $"{str}{(char) ('a' + i)}{str}";
        }

        public char abacaba(int k)
        {
            return str[k - 1];
        }
    }
}


/*
using System;

public class Kata
{
    public char abacaba(int k)
    {
        return (char) ('a' + Math.Log2(k & -k));
    }
}
*/


/*
public class Kata
{
    public char abacaba(int k)
    {
        int c = 0;

        while (k % 2 == 0)
        {
            k /= 2;
            c++;
        }

        return (char) ('a' + c);
    }
}
*/