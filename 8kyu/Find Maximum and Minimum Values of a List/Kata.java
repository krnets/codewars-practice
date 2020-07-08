/*
Your task is to make two functions, max and min that take a(n) array/vector of integers list as input
and outputs, respectively, the largest and lowest number in that array/vector.

        #Examples

        max({4,6,2,1,9,63,-134,566}) returns 566
        min({-52, 56, 30, 29, -54, 0, -110}) returns -110
        max({5}) returns 5
        min({42, 54, 65, 87, 0}) returns 0

        #Notes

        You may consider that there will not be any empty arrays/vectors.
*/

import java.util.Arrays;

/*
public class Kata {

    public int min(int[] list) {
        Arrays.sort(list);
        return list[0];
    }

    public int max(int[] list) {
        Arrays.sort(list);
        return list[list.length - 1];
    }
}*/
/*
public class Kata {

    public int min(int[] list) {
        return Arrays.stream(list).min().getAsInt();
    }

    public int max(int[] list) {
        return Arrays.stream(list).max().getAsInt();
    }
}
*/
public class Kata {

    public int min(int[] list) {
        int smallest = Integer.MAX_VALUE;
        for (int x : list)
            if (x < smallest)
                smallest = x;
        return smallest;
    }

    public int max(int[] list) {
        int largest = Integer.MIN_VALUE;
        for (int x : list)
            if (x > largest)
                largest = x;
        return largest;
    }
}
