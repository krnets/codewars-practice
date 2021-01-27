using System;

public static class Calculator
{
    public static double Execute(double num1, char op, double num2)
    {
        return op switch
        {
            '+' => num1 + num2,
            '-' => num1 - num2,
            '*' => num1 * num2,
            '/' => num2 == 0 ? throw new ArgumentException() : num1 / num2,
            _ => throw new ArgumentException()
        };
    }
}