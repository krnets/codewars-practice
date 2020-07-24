/*
Friday 13th or Black Friday is considered as unlucky day.
Calculate how many unlucky days are in the given year.

        Find the number of Friday 13th in the given year.
        Input: Year as an integer.
        Output: Number of Black Fridays in the year as an integer.

        Examples:

        unluckyDays(2015) == 3
        unluckyDays(1986) == 1

        Note: In Ruby years will start from 1593.
*/


/*
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.Month;
import java.util.Arrays;
*/

import java.time.*;
import java.util.Arrays;

/*
public class Kata {
    public static int unluckyDays(int year) {
        return (int) IntStream.rangeClosed(1, 12)
                .filter(month -> LocalDate.of(year, month, 13).getDayOfWeek().equals(DayOfWeek.FRIDAY))
                .count();
    }
}*/

public class Kata {
    public static long unluckyDays(int year) {
        return Arrays.stream(Month.values())
                .map(month -> LocalDate.of(year, month, 13).getDayOfWeek())
                .filter(DayOfWeek.FRIDAY::equals)
                .count();
    }
}
/*
public class Kata {
    public static long unluckyDays(int year) {
        return Arrays.stream(Month.values())
                .filter(month -> LocalDate.of(year, month, 13).getDayOfWeek().equals(DayOfWeek.FRIDAY))
                .count();
    }
}
*/

/*
public class Kata {
    public static long unluckyDays(int year) {
        return Arrays.stream(Month.values())
                .map(month -> LocalDate.of(year, month, 13))
                .map(LocalDate::getDayOfWeek)
                .filter(DayOfWeek.FRIDAY::equals)
                .count();
    }
}
*/
