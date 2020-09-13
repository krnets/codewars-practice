/*
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 -
(which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation)
should evaluate to 14.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
*/

import java.util.Stack;

public class Calc {
    public double evaluate(String expr) {
        var stack = new Stack<Double>();

        for (String token : expr.split(" ")) {
            switch (token) {
                case "+": stack.push(stack.pop()  + stack.pop()); break;
                case "-": stack.push(-stack.pop() + stack.pop()); break;
                case "*": stack.push(stack.pop()  * stack.pop()); break;
                case "/": stack.push(1 / stack.pop() * stack.pop()); break;
                default:  stack.push(token.isEmpty() ? 0 : Double.parseDouble(token));
            }
        }
        return stack.pop();
    }
}

