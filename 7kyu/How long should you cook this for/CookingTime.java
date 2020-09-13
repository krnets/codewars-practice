/*
You've purchased a ready-meal from the supermarket.

The packaging says that you should microwave it for 4 minutes and 20 seconds,
based on a 600W microwave.

Oh no, your microwave is 800W! How long should you cook this for?!

Input

        You'll be given 4 arguments:
        1. needed power

        The power of the needed microwave.
        Example: "600W"
        2. minutes

        The number of minutes shown on the package.
        Example: 4
        3. seconds

        The number of seconds shown on the package.
        Example: 20
        4. power

        The power of your microwave.
        Example: "800W"

Output

        The amount of time you should cook the meal for formatted as a string.
        Example: "3 minutes 15 seconds"

        Note: the result should be rounded up.

        59.2 sec  -->  60 sec  -->  return "1 minute 0 seconds"
*/


/*
public class CookingTime {
    public static String getTime(String neededPower, int minutes, int seconds, String power) {
        int totalSeconds = 60 * minutes + seconds;
        double powerGivenVsNeeded = (double) Integer.parseInt(power.replace("W", "")) /
                Integer.parseInt(neededPower.replace("W", ""));

        double result = Math.ceil(totalSeconds / powerGivenVsNeeded);
        int resultMin = (int) result / 60;
        int resultSec = (int) result - (resultMin * 60);

        return String.format("%d minutes %d seconds", resultMin, resultSec);
    }
}*/

public class CookingTime {
    public static String getTime(String neededPower, int minutes, int seconds, String power) {
        int totalSeconds = 60 * minutes + seconds;

        var neededWatt = Double.parseDouble(neededPower.replace("W", ""));
        var actualWatt = Double.parseDouble(power.replace("W", ""));

        var factor = actualWatt / neededWatt;
        var durationSeconds = Math.ceil(totalSeconds / factor);

        int resultMin = (int) durationSeconds / 60;
        int resultSec = (int) durationSeconds - (resultMin * 60);

        return String.format("%d minutes %d seconds", resultMin, resultSec);
    }
}
