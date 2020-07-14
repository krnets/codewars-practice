/*
Story

Ben has a very simple idea to make some profit: he buys something and sells it again.
Of course, this wouldn't give him any profit at all if he was simply to buy and sell it
at the same price. Instead, he's going to buy it for the lowest possible price and
sell it at the highest.

Task: Write a function that returns both the minimum and maximum number of the given list/array.

        MinMax.minMax(new int[]{1,2,3,4,5}) == {1,5}
        MinMax.minMax(new int[]{2334454,5}) == {5, 2334454}
        MinMax.minMax(new int[]{1}) == {1, 1}

All arrays or lists will always have at least one element, so you don't need to check the length.
Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.
*/

public class MinMax {
    public static int[] minMax(int[] arr) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int x : arr) {
            if (x > max) max = x;
            if (x < min) min = x;
        }
        return new int[]{min, max};
    }
}
