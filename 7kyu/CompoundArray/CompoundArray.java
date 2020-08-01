/*
You have to create a method "compoundArray" which should take as input two int arrays of different length
and return one int array with numbers of both arrays shuffled one by one.

        Input - {1,2,3,4,5,6} and {9,8,7,6}
        Output - {1,9,2,8,3,7,4,6,5,6}
*/

/*
public class CompoundArray {
    public static int[] compoundArray(int[] a, int[] b) {
        var output = new int[a.length + b.length];
        int index = 0;
        for (int i = 0; i < Math.max(a.length, b.length); i++) {
            if (i < a.length) {
                output[index] = a[i];
                index++;
            }
            if (i < b.length) {
                output[index] = b[i];
                index++;
            }
        }
        return output;
    }
}
*/

public class CompoundArray {
    public static int[] compoundArray(int[] a, int[] b) {
        var output = new int[a.length + b.length];
        for (int i = 0, j = 0; i < Math.max(a.length, b.length); i++) {
            if (i < a.length)
                output[j++] = a[i];
            if (i < b.length)
                output[j++] = b[i];
        }
        return output;
    }
}
