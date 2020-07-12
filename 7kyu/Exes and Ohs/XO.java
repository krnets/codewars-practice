import java.util.stream.Stream;

/*
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. The string can contain any char.

        Examples input/output:

        XO("ooxx") => true
        XO("xooxx") => false
        XO("ooxXm") => true
        XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
        XO("zzoo") => false
*/
/*
public class XO {
    public static boolean getXO(String str) {
        int countX = 0;
        int countO = 0;
        for (char c : str.toUpperCase().toCharArray()) {
            if (c == 'X') countX++;
            if (c == 'O') countO++;
        }
        return countX - countO == 0;
    }
}*/
public class XO {
    public static boolean getXO(String str) {
        var countX = str.toLowerCase().chars().filter(c -> c == 'x').count();
        var countO = str.toLowerCase().chars().filter(c -> c == 'o').count();
        return countX == countO;
    }
}
