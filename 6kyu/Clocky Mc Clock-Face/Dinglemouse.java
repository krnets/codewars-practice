/*
Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.

And because the local council has lost most of our tax money to a Nigerian email scam
there are no funds to fix the clock properly.

Instead, they are asking for volunteer programmers to write some code that tell the time
by only looking at the remaining hour-hand!

Given the angle (in degrees) of the hour-hand, return the time in HH:MM format.
Round down to the nearest minute.

        12:00 = 0 degrees
        03:00 = 90 degrees
        06:00 = 180 degrees
        09:00 = 270 degrees
        12:00 = 360 degrees

        0 <= angle <= 360
*/


/*
public class Dinglemouse {
    public static String whatTimeIsIt(final double angle) {
        double hourAngle = 360 / 12.0;
        double minuteAngle = hourAngle / 60;

        int hours = (int) (angle / hourAngle);

        if (hours == 0) {
            hours = 12;
        }
        int minutes = (int) ((angle / minuteAngle) % 60);

        return String.format("%02d:%02d", hours, minutes);
    }
}*/

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Dinglemouse {
    public static String whatTimeIsIt(final double angle) {
        var hourAngle = 360 / 12.0;
        var minuteAngle = hourAngle / 60;

        int hours = (int) (angle / hourAngle);
        int minutes = (int) ((angle / minuteAngle) % 60);

        var lt = LocalTime.of(hours, minutes);
        var dtf = DateTimeFormatter.ofPattern("hh:mm");

        return dtf.format(lt);
    }
}
