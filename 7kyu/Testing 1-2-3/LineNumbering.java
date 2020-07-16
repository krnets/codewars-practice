/*
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

        Examples:

        number(Arrays.asList()) # => []
        number(Arrays.asList("a", "b", "c")) // => ["1: a", "2: b", "3: c"]
*/


import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
public class LineNumbering {
    public static List<String> number(List<String> lines) {
        var result = new String[lines.size()];
        for (int i = 0; i < lines.size(); i++)
            result[i] = i + 1 + ": " + lines.get(i);
        return Arrays.asList(result);
    }
}*/
/*
public class LineNumbering {
    public static List<String> number(List<String> lines) {
        return IntStream.range(0, lines.size())
                .mapToObj(i -> String.format("%d: %s", i + 1, lines.get(i)))
                .collect(Collectors.toList());
    }
}
*/
/*
public class LineNumbering {
    public static List<String> number(List<String> lines) {
        return IntStream.rangeClosed(1, lines.size())
                .mapToObj(i -> String.format("%d: %s", i, lines.get(i - 1)))
                .collect(Collectors.toList());
    }
}
*/
public class LineNumbering {
    public static List<String> number(List<String> lines) {
        var i = new AtomicInteger();
        return lines.stream()
                .map(line -> {
                    i.getAndIncrement();
                    return i + ": " + line;
                })
                .collect(Collectors.toList());
    }
}
