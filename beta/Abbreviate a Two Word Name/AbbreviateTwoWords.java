/*
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

        The output should be two capital letters with a dot separating them.
        It should look like this:

        Sam Harris => S.H
        Patrick Feeney => P.F
*/

/*
public class AbbreviateTwoWords {
    public static String abbrevName(String name) {
        String[] names = name.split(" ");
        return names[0].substring(0, 1).toUpperCase() + "." + names[1].substring(0, 1).toUpperCase();
    }
}*/
/*
public class AbbreviateTwoWords {
    public static String abbrevName(String name) {
        String[] names = name.split(" ");
        return (names[0].substring(0, 1) + "." + names[1].substring(0, 1)).toUpperCase();
    }
*/
public class AbbreviateTwoWords {
    public static String abbrevName(String name) {
        return (name.charAt(0) + "." + name.charAt(name.indexOf(" ") + 1)).toUpperCase();
    }
}
