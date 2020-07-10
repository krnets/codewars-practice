/*
Complete the function so that it finds the mean of the three scores passed to it and returns
the letter value associated with that grade.

        Numerical Score 	Letter Grade
        90 <= score <= 100 	'A'
        80 <= score < 90 	'B'
        70 <= score < 80 	'C'
        60 <= score < 70 	'D'
        0 <= score < 60 	'F'

        Tested values are all between 0 and 100.
        There is no need to check for negative values or values greater than 100.
*/

public class GrassHopper {
    public static char getGrade(int s1, int s2, int s3) {
        int score = (s1 + s2 + s3) / 3;
        return score < 60 ? 'F' : score < 70 ? 'D' : score < 80 ? 'C' : score < 90 ? 'B' : 'A';
    }
}