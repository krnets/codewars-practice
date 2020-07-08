/*
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Your points are not included in the array of your class's points.
For calculating the average point you may add your point to the given array!
*/

import java.util.stream.IntStream;

/*
public class Kata {
    public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
        double average = IntStream.of(classPoints).sum() / classPoints.length;
        return yourPoints > average ? true : false;
    }
}*/
public class Kata {
    public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
        return IntStream.of(classPoints).average().getAsDouble() < yourPoints;
    }
}
