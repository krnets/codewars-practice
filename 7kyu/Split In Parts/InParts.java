/*
The aim of this kata is to split a given string into different strings of equal size
(note size of strings is passed to the method)

Example: Split the below string into other strings of size #3

             'supercalifragilisticexpialidocious'

              Will return a new string
             'sup erc ali fra gil ist ice xpi ali doc iou s'

Assumptions:  String length is always greater than 0
              String has no spaces
              Size is always positive
*/


public class InParts {
    public static String splitInParts(String s, int partLength) {
        return s.replaceAll("(.{" + partLength + "})(?!$)", "$1 ");
    }
}

/*
public class InParts {
    public static String splitInParts(String s, int partLength) {
        var sb = new StringBuilder(s);
        for (int i = partLength; i < sb.length(); i += partLength + 1)
            sb.insert(i, " ");
        return sb.toString();
    }
}
*/

/*
public class InParts {
    public static String splitInParts(String s, int partLength) {
        if (s.length() <= partLength)
            return s;
        return s.substring(0, partLength) + " " + splitInParts(s.substring(partLength), partLength);
    }
}
*/

/*
public class InParts {
    public static String splitInParts(String s, int partLength) {
        var res = new StringBuilder();
        for (int i = 0; i < s.length(); i += partLength) {
            res.append(s, i, Math.min(i + partLength, s.length())).append(" ");
        }
        return res.toString().trim();
    }
}
*/
