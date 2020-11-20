import java.util.*;

public class DirReduction {

    public static String[] dirReduc(String[] arr) {
        var stack = new Stack<>();
        var opposites = new HashMap<>();
        var directions = List.of("NORTH", "EAST", "SOUTH", "WEST");

        for (int i = 0; i < directions.size(); i++)
            opposites.put(directions.get(i), directions.get((i + 2) % directions.size()));

        for (String s : arr)
            if (stack.isEmpty()) {
                stack.push(s);
            } else if (opposites.get(stack.peek()).equals(s)) {
                stack.pop();
            } else {
                stack.push(s);
            }
        return stack.toArray(new String[0]);
    }
}
