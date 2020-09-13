/*
In English and programming, groups can be made using symbols such as () and {} that change meaning.
However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping.
For instance, the following groups are done correctly:

        ({})
        [[]()]
        [{()}]

The next are done incorrectly:

        {(})
        ([]
        [])

A correct string cannot close groups in the wrong order, open a group but fail to close it,
or close a group before it is opened.

Your function will take an input string that may contain any of the symbols (), {} or [] to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.
*/

/*
public class Groups {
    public static boolean groupCheck(String s) {
        var pattern = "((\\(\\))|(\\{})|(\\[]))";

        for (int i = s.length() / 2; i > 0; i--) {
            s = s.replaceAll(pattern, "");
        }
        return s.isEmpty();
    }
}*/

import java.util.Map;
import java.util.Stack;

/*
public class Groups {
    private static final Map<Character, Character> BRACKETS = Map.of('(', ')', '{', '}', '[', ']');

    public static boolean groupCheck(String s) {
        var stack = new Stack<Character>();

        for (char c : s.toCharArray()) {
            if (BRACKETS.containsKey(c))
                stack.push(c);
            else if (!stack.isEmpty() && c == BRACKETS.get(stack.peek()))
                stack.pop();
            else return false;
        }
        return stack.isEmpty();
    }
}
*/
public class Groups {
    private static final Map<Character, Character> BRACKETS = Map.of('(', ')', '{', '}', '[', ']');

    public static boolean groupCheck(String s) {
        var stack = new Stack<Character>();

        for (char c : s.toCharArray()) {
            if (BRACKETS.containsKey(c))
                stack.push(c);
            else if (stack.isEmpty() || BRACKETS.get(stack.pop()) != c)
                return false;
        }
        return stack.isEmpty();
    }
}
