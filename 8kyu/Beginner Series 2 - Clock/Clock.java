/*
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

        Your task is to make 'Past' function which returns time converted to milliseconds.

        Past(0, 1, 1) == 61000

        Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59
*/

/*
public class Clock {
    public static int Past(int h, int m, int s) {
        return h * 60 * 60 * 1000 + m * 60 * 1000 + s * 1000;
    }
}*/
/*
public class Clock {
    public static int Past(int h, int m, int s) {
        return (int) (1000 * (h * Math.pow(60, 2) + m * 60 + s));
    }
}
*/

import java.time.Duration;

public class Clock {
    public static int Past(int h, int m, int s) {
        return (int) Duration.ofHours(h).plusMinutes(m).plusSeconds(s).toMillis();
    }
}
