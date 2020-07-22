/*
Input:
        a string strng
        an array of strings arr

Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

        a boolean true if all rotations of strng are included in arr (C returns 1)
        false otherwise (C returns 0)

Examples:
        contain_all_rots(
        "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

        contain_all_rots(
        "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)

Note:   Though not correct in a mathematical sense

        we will consider that there are no rotations of strng == ""
        and for any array arr: contain_all_rots("", arr) --> true
*/


/*
import java.util.ArrayList;
import java.util.List;

public class Rotations {
    public static boolean containAllRots(String strng, List<String> arr) {
        var rots = new ArrayList<String>();
        for (int i = 0; i < strng.length(); i++) {
            var temp = strng.substring(1) + strng.charAt(0);
            rots.add(temp);
            strng = temp;
        }
        return arr.containsAll(rots);
    }
}*/

import java.util.List;
import java.util.stream.IntStream;

public class Rotations {
    public static boolean containAllRots(String strng, List<String> arr) {
        return IntStream.range(0, strng.length())
                .mapToObj(i -> strng.substring(i) + strng.substring(0, i))
                .allMatch(arr::contains);
    }
}
