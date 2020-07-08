/*
Our football team finished the championship. The result of each match look like "x:y".
Results of all matches are recorded in the collection.

        For example: ["3:1", "2:2", "0:1", ...]

        Write a function that takes such collection and counts the points of our team in the championship.
        Rules for counting points for each match:

        if x>y - 3 points
        if x<y - 0 point
        if x=y - 1 point

        Notes:

        there are 10 matches in the championship
        0 <= x <= 4
        0 <= y <= 4
*/
/*
public class TotalPoints {
    public static int points(String[] games) {
        int total = 0;
        for (int i = 0; i < 10; i++) {
            if (Integer.parseInt(games[i].substring(0, 1)) > Integer.parseInt(games[i].substring(2, 3)))
                total += 3;
            if (Integer.parseInt(games[i].substring(0, 1)) == Integer.parseInt(games[i].substring(2, 3)))
                total += 1;
        }
        return total;
    }
}*/
/*
public class TotalPoints {
    public static int points(String[] games) {
        int total = 0;
        for (int i = 0; i < games.length; i++) {
            int x = Integer.parseInt(games[i].substring(0, 1));
            int y = Integer.parseInt(games[i].substring(2, 3));
            if (x > y) total += 3;
            if (x == y) total += 1;
        }
        return total;
    }
}
*/
public class TotalPoints {
    public static int points(String[] games) {
        int total = 0;
        for (String s : games) {
            Character x = s.charAt(0);
            Character y = s.charAt(2);
            if (x > y) total += 3;
            if (x == y) total += 1;
        }
        return total;
    }
}
