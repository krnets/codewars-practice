using System;
using System.Collections.Generic;

public class Brace
{
    private static readonly Dictionary<char, char> ClosingPair = new Dictionary<char, char>()
        {{'(', ')'}, {'{', '}'}, {'[', ']'}};

    private static bool IsClosing(char peek, char c) => ClosingPair.ContainsKey(peek) && ClosingPair[peek] == c;

    public static bool validBraces(String braces)
    {
        var stack = new Stack<char>();

        foreach (char c in braces)
            if (stack.Count > 0 && IsClosing(stack.Peek(), c))
                stack.Pop();
            else stack.Push(c);

        return stack.Count == 0;
    }
}