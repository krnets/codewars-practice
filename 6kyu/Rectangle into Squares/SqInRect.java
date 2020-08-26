/*
The drawing below gives an idea of how to cut a given "true" rectangle into squares
("true" rectangle meaning that the two dimensions are different).

Can you translate this drawing into an algorithm?

You will be given two dimensions

        a positive integer length (parameter named lng)
        a positive integer width (parameter named wdth)

You will return an array or a string with the size of each of the squares.

        sqInRect(5, 3) should return [3, 2, 1, 1]
        sqInRect(3, 5) should return [3, 2, 1, 1]

        Your result and the reference test solution are compared by strings.

Notes:  lng == wdth as a starting case would be an entirely different problem
        and the drawing is planned to be interpreted with lng != wdth.
        (See kata, Square into Squares. Protect trees!
        http://www.codewars.com/kata/54eb33e5bc1a25440d000891 for this problem).

        When the initial parameters are so that lng == wdth,
        the solution [lng] would be the most obvious but not in the spirit of this kata
        so, in that case, return null
*/

import java.util.ArrayList;
import java.util.List;

public class SqInRect {
    public static List<Integer> sqInRect(int lng, int wdth) {
        if (lng == wdth)
            return null;

        var squares = new ArrayList<Integer>();

        while (lng * wdth > 0) {
            if (lng > wdth) {
                squares.add(lng - (lng - wdth));
                lng = lng - wdth;
            } else {
                squares.add(wdth - (wdth - lng));
                wdth = wdth - lng;
            }
        }
        return squares;
    }
}
/*
public class SqInRect {
    public static List<Integer> sqInRect(int lng, int wdth) {
        if (lng == wdth)
            return null;

        var squares = new ArrayList<Integer>();
        int diff;

        while (lng * wdth > 0) {
            if (lng > wdth) {
                diff = lng - wdth;
                squares.add(lng - diff);
                lng = diff;
            } else {
                diff = wdth - lng;
                squares.add(wdth - diff);
                wdth = diff;
            }
        }
        return squares;
    }
}
*/
