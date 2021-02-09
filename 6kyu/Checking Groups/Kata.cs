using System.Collections.Generic;

public static class Groups
{
    public static bool Check(string input)
    {
        var stack = new Stack<char>();
        var matchingPairs = new Dictionary<char, char> {{'}', '{'}, {']', '['}, {')', '('}};

        foreach (var c in input)
        {
            if (matchingPairs.ContainsKey(c))
            {
                stack.TryPop(out var topChar);

                if (matchingPairs[c] != topChar)
                    return false;
            }
            else stack.Push(c);
        }

        return stack.Count == 0;
    }
}