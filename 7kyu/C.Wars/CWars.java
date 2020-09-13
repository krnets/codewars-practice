/*
Normally we have firstname, middle and the last name
but there may be more than one word in a name like a South Indian one.

Similar to those kinda names we need to initialize the names.

See the pattern below:

        initials('code wars') => returns C.Wars
        initials('Barack Hussain obama') => returns B.H.Obama

Complete the function initials.
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
public class CWars {
    public static String initials(String name) {
        var arr = name.split(" ");

        return IntStream.range(0, arr.length)
                .mapToObj(i -> (i != arr.length - 1) ? arr[i].substring(0, 1).toUpperCase() :
                        arr[i].substring(0, 1).toUpperCase() + arr[i].substring(1))
                .collect(Collectors.joining("."));
    }
}*/

public class CWars {
    public static String initials(String name) {
        var arr = name.split(" ");

        return IntStream.range(0, arr.length)
                .mapToObj(i -> arr[i].substring(0, 1).toUpperCase() +
                        ((i == arr.length - 1) ? arr[i].substring(1) : ""))
                .collect(Collectors.joining("."));
    }
}
