/*
Create a method, that corrects a given time string.
There was a problem in addition, so many of the time strings are broken.
Time-Format is european. So from "00:00:00" to "23:59:59".

        Some examples:

        "09:10:01" -> "09:10:01"
        "11:70:10" -> "12:10:10"
        "19:99:99" -> "20:40:39"
        "24:01:01" -> "00:01:01"

        If the input-string is null or empty return exactly this value
*/

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;

public class Solution {
    public static String timeCorrect(String timestring) {
        if (timestring == null || !timestring.matches("^\\d{2}:\\d{2}:\\d{2}$"))
            return null;

        var arr = Arrays.stream(timestring.split(":"))
                .mapToInt(Integer::parseInt).toArray();

        return LocalTime.of(0, 0, 0)
                .plusHours(arr[0])
                .plusMinutes(arr[1])
                .plusSeconds(arr[2])
                .format(DateTimeFormatter.ISO_LOCAL_TIME);
    }
}

/*
public class Solution {
    public static String timeCorrect(String timestring) {
        if (timestring == null || !timestring.matches("^\\d{2}:\\d{2}:\\d{2}$")) return null;
        var units = Arrays.stream(timestring.split(":")).mapToInt(Integer::parseInt).toArray();
        var seconds = units[2] % 60;
        var minutes = (units[1] + units[2] / 60) % 60;
        var hours = (units[0] + (units[1] + units[2] / 60) / 60) % 24;
        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }
}
*/

/*
public class Solution {
    public static String timeCorrect(String timestring) {
        if (timestring == null || !timestring.matches("^\\d{2}:\\d{2}:\\d{2}$")) return null;
        var units = Arrays.stream(timestring.split(":")).mapToInt(Integer::parseInt).toArray();
        var seconds = (units[2] + units[1] * 60 + units[0] * 60 * 60) % (24 * 60 * 60);
        return LocalTime.ofSecondOfDay(seconds).format(DateTimeFormatter.ISO_LOCAL_TIME);
    }
}*/
