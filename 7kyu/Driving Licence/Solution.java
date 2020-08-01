/*
Task : The UK driving number is made up from the personal details of the driver.
The individual letters and digits can be code using the below information

Rules
        1–5: The first five characters of the surname (padded with 9s if less than 5 characters)

        6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

        7–8: The month of birth
        (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)

        9–10: The date within the month of birth

        11: The year digit from the year of birth (e.g. for 1987 it would be 7)

        12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name

        14: Arbitrary digit – usually 9, but decremented to differentiate drivers
        with the first 13 characters in common. We will always use 9

        15–16: Two computer check digits. We will always use "AA"


        Your task is to code a UK driving license number using an Array of data.
        The Array will look like

        data = {"John","James","Smith","01-Jan-2000","M"};

        Where the elements are as follows
        0 = Forename

        1 = Middle Name (if any)

        2 = Surname

        3 = Date of Birth (In the format Day Month Year, this could include the full Month name
        or just shorthand ie September or Sep)

        4 = M-Male or F-Female

        You will need to output the full 16 digit driving license number.
*/

import java.util.Arrays;

public class Solution {
    public static String driver(final String[] data) {
        var firstName = data[0];
        var middleName = data[1];
        var surname = data[2] + "99999";
        var dateOfBirth = data[3];
        var gender = data[4];
        var months = Arrays.asList("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec");
        var licence = new StringBuilder();

        licence.append(surname, 0, 5);
        licence.append(dateOfBirth, dateOfBirth.length() - 2, dateOfBirth.length() - 1);

        var monthOfBirth = months.indexOf(dateOfBirth.substring(3, 6)) + 1;
        if (gender.equals("F"))
            licence.append(("" + (monthOfBirth + 50)), 0, 2);
        else
            licence.append((monthOfBirth < 10 ? "0" + monthOfBirth : "" + monthOfBirth), 0, 2);

        licence.append(dateOfBirth, 0, 2);
        licence.append(dateOfBirth, dateOfBirth.length() - 1, dateOfBirth.length());
        licence.append(firstName, 0, 1).append((middleName + "9"), 0, 1);
        licence.append("9" + "AA");

        return licence.toString().toUpperCase();
    }
}
