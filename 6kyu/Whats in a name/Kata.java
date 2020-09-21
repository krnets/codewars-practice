/*
What's in a name?
..Or rather, what's a name in?
For us, a particular string is where we are looking for a name.

Task:   Test whether or not the string contains all of the letters which spell a given name, in order.
        The format
        A function passing two strings, searching for one (the name) within the other.
        nameInStr(str, name){ return true || false }

Examples

        nameInStr("Across the rivers", "chris") --> true
        ^      ^  ^^   ^
        c      h  ri   s

        Contains all of the letters in "chris", in order.


        nameInStr("Next to a lake", "chris") --> false

        Contains none of the letters in "chris".


        nameInStr("Under a sea", "chris") --> false
        ^   ^
        r   s

        Contains only some of the letters in "chris".


        nameInStr("A crew that boards the ship", "chris") --> false
        cr    h              s i
        cr                h  s i
        c     h      r       s i
        ...

        Contains all of the letters in "chris", but not in order.


        nameInStr("A live son", "Allison") --> false
        ^ ^^   ^^^
        A li   son

        Contains all of the correct letters in "Allison", in order,
        but not enough of all of them (missing an 'l').

Note:   testing will not be case-sensitive.
*/

/*
public class Kata {
    public static boolean nameInStr(String str, String name) {
        int count = 0;

        for (int i = 0, j = 0; i < str.length(); i++) {
            if (str.charAt(i) == name.charAt(j)) {
                count++;
                j++;
            }
        }
        return name.length() == count;
    }
}*/

public class Kata {
    public static boolean nameInStr(String str, String name) {
        int i = 0;

        for (char c : str.toCharArray()) {
            if (c == name.charAt(i))
                i++;
        }
        return i == name.length();
    }
}

/*public class Kata {
    public static boolean nameInStr(String str, String name) {
        return str.matches(name.replace("", ".*"));
    }
}*/
