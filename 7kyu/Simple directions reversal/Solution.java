/*
In this Kata, you will be given directions and your task will be to find your way back.

        solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"])
           => ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']

        solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr'])
          =>  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']

        More examples in test cases.
*/

import java.util.Stack;

class Solution {
    public static String[] solve(String[] arr) {
        var wayBack = new String[arr.length];
        var stack = new Stack<String>();

        for (String s : arr) {
            var split = s.split(" ", 2);
            stack.push(split[0]);
            stack.push(split[1]);
        }
        wayBack[0] = "Begin " + stack.pop();

        for (int i = 1; i < wayBack.length; i++) {
            var direction = stack.pop();
            direction = direction.equals("Right") ? "Left" : "Right";
            wayBack[i] = String.format("%s %s", direction, stack.pop());
        }
        return wayBack;
    }
}