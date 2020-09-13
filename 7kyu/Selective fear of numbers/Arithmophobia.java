/*
The number I'm afraid of depends on which day of the week it is...

        Monday --> 12

        Tuesday --> numbers greater than 95

        Wednesday --> 34

        Thursday --> 0

        Friday --> numbers divisible by 2

        Saturday --> 56

        Sunday --> 666 or -666

Write a function which takes a string (day of the week) and an integer (number to be tested)
so it tells the doctor if I'm afraid or not.

Return a boolean
*/

public class Arithmophobia {
    static public boolean AmIAfraid(final String day, final int num) {
        switch (day) {
            case "Monday"    : return num == 12;
            case "Tuesday"   : return num > 95;
            case "Wednesday" : return num == 34;
            case "Thursday"  : return num == 0;
            case "Friday"    : return num % 2 == 0;
            case "Saturday"  : return num == 56;
            case "Sunday"    : return Math.abs(num) == 666;
            default          : return false;
        }
    }
}