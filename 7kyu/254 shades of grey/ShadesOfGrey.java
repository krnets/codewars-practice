/*
Why would we want to stop to only 50 shades of grey? Let's see to how many we can go.

Write a function that takes a number n as a parameter and return an array containing n shades of grey
in hexadecimal code (#aaaaaa for example). The array should be sorted in ascending order starting
with #010101, #020202, etc. (using lower case letters).

As a reminder, the grey color is composed by the same number of red, green and blue:
#010101, #aeaeae, #555555, etc. Also, #000000 and #ffffff are not accepted values.

When n is negative, just return an empty array.
If n is higher than 254, just return an array of 254 elements.
*/

import java.util.ArrayList;
import java.util.stream.IntStream;

/*
public class ShadesOfGrey {
    static String[] shadesOfGrey(int num) {
        var result = new ArrayList<String>();
        for (int i = 1; i < Math.min(num, 254) + 1; i++) {
            result.add("#" + String.format("%02x", i).repeat(3));
        }
        return num < 1 ? new String[0] : result.toArray(new String[0]);
    }
}*/
/*
public class ShadesOfGrey {
    static String[] shadesOfGrey(int num) {
        var result = new ArrayList<String>();
        for (int i = 1; i < Math.min(num, 254) + 1; i++)
            result.add("#" + String.format("%02x", i).repeat(3));
        return result.toArray(new String[0]);
    }
}
*/
public class ShadesOfGrey {
    static String[] shadesOfGrey(int num) {
        return IntStream.rangeClosed(1, Math.min(num, 254))
                .mapToObj(i -> "#" + String.format("%02x", i).repeat(3))
                .toArray(String[]::new);
    }
}
