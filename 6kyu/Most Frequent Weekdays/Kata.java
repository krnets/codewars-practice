/*
What is your favourite day of the week?
Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001).
You should return the most frequent day(s) of the week in that year.
The result has to be a list of days sorted by the order of days in week
(e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']).

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Preconditions:

        Week starts on Monday.
        Year is between 1583 and 4000.
        Calendar is Gregorian.

Example:

        Kata.mostFrequentDays(2427) => {"Friday"}
        Kata.mostFrequentDays(2185) => {"Saturday"}
        Kata.mostFrequentDays(2860) => {"Thursday", "Friday"}
*/

/*
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class Kata {
    public static String[] mostFrequentDays(int year) {
        int mostFrequent = 0;
        var dateCursor = LocalDate.of(year, 1, 1);
        var firstDayNextYear = LocalDate.of(year + 1, 1, 1);

        var daysOfWeekInYear = new ArrayList<>();
        var frequencyMap = new HashMap<String, Integer>();
        var mostFrequentDays = new ArrayList<String>();

        while (dateCursor.isBefore(firstDayNextYear)) {
            daysOfWeekInYear.add(dateCursor.getDayOfWeek());
            dateCursor = dateCursor.plusDays(1);
        }
        for (DayOfWeek day : DayOfWeek.values()) {
            frequencyMap.put(day.toString(), Collections.frequency(daysOfWeekInYear, day));
        }
        for (Integer val : frequencyMap.values()) {
            mostFrequent = Math.max(mostFrequent, val);
        }
        for (var e : frequencyMap.entrySet()) {
            if (mostFrequent == e.getValue())
                mostFrequentDays.add(e.getKey());
        }
        return Arrays.stream(DayOfWeek.values())
                .map(Enum::toString)
                .filter(mostFrequentDays::contains)
                .map(x -> x.charAt(0) + x.substring(1).toLowerCase())
                .toArray(String[]::new);
    }
}
*/

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.*;

public class Kata {
    public static String[] mostFrequentDays(int year) {
        int mostFrequent = 0;
        var dateCursor = LocalDate.of(year, 1, 1);
        var firstDayNextYear = LocalDate.of(year + 1, 1, 1);

        var daysOfWeekInYear = new ArrayList<>();
        var frequencyMap = new HashMap<String, Integer>();
        var mostFrequentDays = new ArrayList<String>();

        while (dateCursor.isBefore(firstDayNextYear)) {
            var x = dateCursor.getDayOfWeek().getDisplayName(TextStyle.FULL, Locale.ENGLISH);
            daysOfWeekInYear.add(x);
            dateCursor = dateCursor.plusDays(1);
        }
        for (DayOfWeek day : DayOfWeek.values()) {
            var x = day.getDisplayName(TextStyle.FULL, Locale.ENGLISH);
            frequencyMap.put(x, Collections.frequency(daysOfWeekInYear, x));
        }
        for (Integer val : frequencyMap.values()) {
            mostFrequent = Math.max(mostFrequent, val);
        }
        for (var e : frequencyMap.entrySet()) {
            if (mostFrequent == e.getValue())
                mostFrequentDays.add(e.getKey());
        }
        return Arrays.stream(DayOfWeek.values())
                .map(x -> x.getDisplayName(TextStyle.FULL, Locale.ENGLISH))
                .filter(mostFrequentDays::contains)
                .toArray(String[]::new);
    }
}
