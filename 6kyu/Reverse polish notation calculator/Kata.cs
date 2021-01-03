using System;
using System.Collections.Generic;

public class Calc
{
    public double evaluate(String expr)
    {
        double result = 0;

        if (string.IsNullOrEmpty(expr))
            return result;

        var stack = new Stack<double>();
        var tokens = expr.Split();

        foreach (var token in tokens)
            if ("+-/*".Contains(token) && stack.Count > 1)
            {
                var b = stack.Pop();
                var a = stack.Pop();

                result = token switch
                {
                    "+" => a + b,
                    "-" => a - b,
                    "*" => a * b,
                    "/" => a / b,
                    _ => result
                };

                stack.Push(result);
            }
            else
                stack.Push(double.Parse(token));

        return stack.Count == 1 ? stack.Pop() : result;
    }
}