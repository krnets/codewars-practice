/*
Your colleagues have been looking over you shoulder.
When you should have been doing your boring real job,
you've been using the work computers to smash in endless hours of codewars.

In a team meeting, a terrible, awful person declares to the group
that you aren't working. You're in trouble. You quickly have to
gauge the feeling in the room to decide whether or not you should
gather your things and leave.

Given a Person array (meet) containing team members, you need to assess
the overall happiness rating of the group.

If <= 5, return "Get Out Now!".
Else return "Nice Work Champ!".

Happiness rating will be total score / number of people in the room.

Note that your boss is in the room (boss), their score is worth double it's face value
(but they are still just one person!).
*/

import java.util.Arrays;

class Person {
    final String name;    // team member's name
    final int happiness;  // happiness rating out of 10

    Person(String name, int happiness) {
        this.name = name;
        this.happiness = happiness;
    }
}

/*
public class TheOffice {
    public static String outed(Person[] meet, String boss) {
        return Arrays.stream(meet)
                .mapToInt(p -> p.name.equals(boss) ? p.happiness * 2 : p.happiness)
                .average().orElse(0) > 5 ? "Nice Work Champ!" : "Get Out Now!";
    }
}*/
public class TheOffice {
    public static String outed(Person[] meet, String boss) {
        return Arrays.stream(meet)
                .mapToInt(p -> p.happiness * (p.name.equals(boss) ? 2 : 1))
                .average().orElse(0) > 5 ? "Nice Work Champ!" : "Get Out Now!";
    }
}
