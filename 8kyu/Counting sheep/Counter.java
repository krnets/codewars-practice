import java.util.Arrays;

/*
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).

        [true,  true,  true,  false,
        true,  true,  true,  true ,
        true,  false, true,  false,
        true,  false, false, true ,
        true,  true,  true,  true ,
        false, false, true,  true]

        The correct answer would be 17.

        Hint: Don't forget to check for bad values like null/undefined
*/
/*
public class Counter {
    public int countSheeps(Boolean[] arrayOfSheeps) {
        int counter = 0;
        for (Boolean x : arrayOfSheeps)
            if (x != null && x) counter++;
        return counter;
    }
}*/

public class Counter {
    public int countSheeps(Boolean[] arrayOfSheeps) {
        return (int) Arrays.stream(arrayOfSheeps).filter(x -> x != null && x == true).count();
    }
}
