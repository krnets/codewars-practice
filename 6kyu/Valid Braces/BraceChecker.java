/*
Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters:
brackets [], and curly braces {}.

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces:
()[]{}.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.

        "(){}[]"   =>  True
        "([{}])"   =>  True
        "(}"       =>  False
        "[(])"     =>  False
        "[({})](]" =>  False
*/

/*
public class BraceChecker {
    public boolean isValid(String braces) {
        for (int i = braces.length() / 2; i > 0; i--) {
            braces = braces.replaceAll("\\(\\)|\\{}|\\[]", "");
        }
        return braces.isEmpty();
    }
}
*/

import java.util.Map;
import java.util.Stack;

public class BraceChecker {
    static Map<Character, Character> closingPair = Map.of('(', ')', '{', '}', '[', ']');

    public boolean isValid(String braces) {
        var stack = new Stack<Character>();
        for (char c : braces.toCharArray()) {
            if (stack.size() > 0 && isClosing(stack.peek(), c))
                stack.pop();
            else stack.push(c);
        }
        return stack.isEmpty();
    }

    private boolean isClosing(Character peek, char c) {
        return closingPair.getOrDefault(peek, ' ').equals(c);
    }
}

