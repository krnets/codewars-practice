/*
Have you heard about the myth that if you fold a paper enough times,
you can reach the moon with it? Sure you do, but exactly how many?
Maybe it's time to write a program to figure it out.

        You know that a piece of paper has a thickness of 0.0001m.
        Given distance in units of meters, calculate how many times you have to fold the paper
        to make the paper reach this distance.
        (If you're not familiar with the concept of folding a paper:
        Each fold doubles its total thickness.)

        Note: Of course you can't do half a fold. You should know what this means ;P

        Also, if somebody is giving you a negative distance, it's clearly bogus and
        you should yell at them by returning null.
*/

/*
public class PaperFolder {
    public static Long fold(Double distance) {
        if (distance < 0) return null;
        double paperThickness = 0.0001;
        int countFolds = 0;
        while (paperThickness < distance) {
            paperThickness *= 2;
            countFolds++;
        }
        return Long.valueOf(countFolds);
    }
}
*/

/*
public class PaperFolder {
    public static Long fold(Double distance) {
        if (distance < 0) return null;
        long countFolds = 0;
        for (double thickness = 0.0001; thickness < distance; thickness *= 2)
            countFolds++;
        return countFolds;
    }
}
*/
/*
public class PaperFolder {
    public static Long fold(Double distance) {
        return distance < 0 ? null : distance <= 0.0001 ? 0 : 1 + fold(distance / 2);
    }
}
*/
public class PaperFolder {
    public static Long fold(Double distance) {
        long count = 0;
        while (distance > (0.0001 * Math.pow(2, count++))) ;
        return count - 1;
    }
}