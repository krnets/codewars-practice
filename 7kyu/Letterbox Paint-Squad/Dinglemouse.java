/*
Story

You and a group of friends are earning some extra money in the school holidays by re-painting
the numbers on people's letterboxes for a small fee.

Since there are 10 of you in the group each person just concentrates on painting one digit!
For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...

But at the end of the day you realise not everybody did the same amount of work.

To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.

Kata Task
    Given the start and end letterbox numbers, write a method
    to return the frequency of all 10 digits painted.

Example
        For start = 125, and end = 132
        The letterboxes are

        125 = 1, 2, 5
        126 = 1, 2, 6
        127 = 1, 2, 7
        128 = 1, 2, 8
        129 = 1, 2, 9
        130 = 1, 3, 0
        131 = 1, 3, 1
        132 = 1, 3, 2

        The digit frequencies are 1 x 0, 9 x 1, 6 x 2 etc...
        and so the method would return [1,9,6,3,0,1,1,1,1,1]
Notes
        0 < start <= end
        In C, the returned value will be free'd.
*/

/*
import static java.lang.Integer.parseInt;
import static java.util.stream.Collectors.*;
import static java.util.stream.IntStream.*;

public class Dinglemouse {
    public static int[] paintLetterboxes(final int start, final int end) {
        var digits = new int[10];
        var letterboxNumbers = rangeClosed(start, end).mapToObj(String::valueOf).collect(joining());
        for (var s : letterboxNumbers.split("")) {
            digits[parseInt(s)]++;
        }
        return digits;
    }
}
*/

/*
import static java.util.stream.Collectors.*;
import static java.util.stream.IntStream.*;

public class Dinglemouse {
    public static int[] paintLetterboxes(final int start, final int end) {
        return range(0, 10)
                .map(i -> Math.toIntExact(rangeClosed(start, end)
                        .flatMap(j -> String.valueOf(j).chars().map(Character::getNumericValue))
                        .boxed()
                        .collect(groupingBy(Integer::valueOf, counting()))
                        .getOrDefault(i, 0L)))
                .toArray();
    }
}
*/

public class Dinglemouse {
    public static int[] paintLetterboxes(final int start, final int end) {
        var digits = new int[10];
        for (int i = start; i <= end; i++) {
            int num = i;
            while (num > 0) {
                digits[num % 10]++;
                num /= 10;
            }
        }
        return digits;
    }
}
