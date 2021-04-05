/*using System.Collections.Generic;

public class Parentheses
{
    public static bool ValidParentheses(string input)
    {
        var stack = new Stack<char>();

        foreach (char c in input)
            if (c == '(')
                stack.Push(c);
            else if (c == ')')
                if (stack.Count > 0)
                    stack.Pop();
                else return false;


        return stack.Count == 0;
    }
}*/

public class Parentheses
{
    public static bool ValidParentheses(string input)
    {
        int balance = 0;

        foreach (char c in input)
            if (c == '(')
                balance++;
            else if (c == ')')
                if (balance <= 0)
                    return false;
                else balance--;

        return balance == 0;
    }
}