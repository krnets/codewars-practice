/*
Write a simple parser that will parse and run Deadfish.

        Deadfish has 4 commands, each 1 character long:

        i increments the value (initially 0)
        d decrements the value
        s squares the value
        o outputs the value into the return array

        Invalid characters should be ignored.

        Deadfish.parse("iiisdoso") =- new int[] {8, 64};
*/

/*
import java.util.ArrayList;

public class DeadFish {
    public static int[] parse(String data) {
        int val = 0;
        var result = new ArrayList<Integer>();
        for (char c : data.toCharArray()) {
            switch (c) {
                case 'i': val++; break;
                case 'd': val--; break;
                case 's': val *= val; break;
                case 'o': result.add(val);
            }
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}
*/

public class DeadFish {
    public static int[] parse(String data) {
        int value = 0;
        var result = new int[data.replaceAll("[^o]", "").length()];
        for (int i = 0, j = 0; i < data.length(); i++) {
            switch (data.charAt(i)) {
                case 'i': value++; break;
                case 'd': value--; break;
                case 's': value *= value; break;
                case 'o': result[j++] = value;
            }
        }
        return result;
    }
}
