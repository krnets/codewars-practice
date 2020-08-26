/*
A family of kookaburras are in my backyard.

        I can't see them all, but I can hear them!
        How many kookaburras are there?
Hint

        The trick to counting kookaburras is to listen carefully

        The males go HaHaHa...
        The females go hahaha...

        And they always alternate male/female

Note : No validation is necessary; only valid input will be passed
*/

import java.util.regex.Pattern;

public class Dinglemouse {
    public static int kookaCounter(final String laughing) {
        return (int) Pattern.compile("(Ha)+|(ha)+")
                .matcher(laughing)
                .results()
                .count();
    }
}