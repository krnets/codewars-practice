/*
Every now and then people in the office moves teams or departments.
Depending what people are doing with their time they can become more or less boring.
Time to assess the current team.

You will be provided with an array of Person objects with each instance containing
the name and department for a staff member.

Each department has a different boredom assessment score, as follows:

        accounts = 1
        finance = 2
        canteen = 10
        regulation = 3
        trading = 6
        change = 6
        IS = 8
        retail = 5
        cleaning = 4
        pissing about = 25

Depending on the cumulative score of the team, return the appropriate sentiment:

        <=80: "kill me now"
        < 100 & > 80: "i can handle this"
        100 or over: "party time!!"
*/

import java.util.Map;
import java.util.stream.Stream;

class Person {
    public final String name;        // name of the staff member
    public final String department;  // department they work in

    Person(String name, String department) {
        this.name = name;
        this.department = department;
    }
}

public class TheOffice {
    static Map<String, Integer> scores = Map.of(
            "accounts", 1,
            "finance", 2,
            "canteen", 10,
            "regulation", 3,
            "trading", 6,
            "change", 6,
            "IS", 8,
            "retail", 5,
            "cleaning", 4,
            "pissing about", 25);

    public static String boredom(Person[] staff) {
        var sum = Stream.of(staff).mapToInt(x -> scores.get(x.department)).sum();
        return sum <= 80 ? "kill me now" : sum < 100 ? "i can handle this" : "party time!!";
    }
}

/*
public class TheOffice {
    public static String boredom(Person[] staff) {
        return java.util.Optional.of(staff)
                .map(o -> java.util.Arrays.stream(staff)
                        .map(s -> s.department)
                        .mapToInt(d -> "JHYAB  EDFFC"
                                .charAt((d.charAt(0) * 4 + d.charAt(1) * 5 + d.length()) % 12) - '@')
                        .peek(System.out::println)
                        .sum())
                .map(x -> x > 99 ? "party time!!" : x > 80 ? "i can handle this" : "kill me now")
                .get();
    }
}
*/
