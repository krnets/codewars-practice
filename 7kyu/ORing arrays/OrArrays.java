/*
It started as a discussion with a friend, who didn't fully grasp some way of setting defaults,
but I thought the idea was cool enough for a beginner kata:

binary OR each matching element of two given arrays of integers
and give the resulting ORed array [starts to sound like a tonguetwister, doesn't it?].

If one array is shorter than the other, use the optional third parametero (defaulted to 0)
to OR the unmatched elements.

For example:

        orArrays([1,2,3],[1,2,3]) == [1,2,3]
        orArrays([1,2,3],[4,5,6]) == [5,7,7]
        orArrays([1,2,3],[1,2]) == [1,2,3]
        orArrays([1,2],[1,2,3]) == [1,2,3]
        orArrays([1,2,3],[1,2,3],3) == [1,2,3]
*/

/*
import java.util.stream.IntStream;

public class OrArrays {
    public static int[] orArrays(int[] arr1, int[] arr2, int... param) {
        int defParam = param.length > 0 ? param[0] : 0;

        return IntStream.range(0, Math.max(arr1.length, arr2.length))
                .map(i -> (i < arr1.length ? arr1[i] : defParam) | (i < arr2.length ? arr2[i] : defParam))
                .toArray();
    }
}*/

import java.util.Arrays;

public class OrArrays {
    public static int[] orArrays(int[] arr1, int[] arr2) {
        return orArrays(arr1, arr2, 0);
    }

    public static int[] orArrays(int[] arr1, int[] arr2, int fill) {
        int maxLength = Math.max(arr1.length, arr2.length);
        var dupArr1 = Arrays.copyOf(arr1, maxLength);
        var dupArr2 = Arrays.copyOf(arr2, maxLength);
        var result = new int[maxLength];

        if (arr1.length < arr2.length)
            Arrays.fill(dupArr1, arr1.length, maxLength, fill);
        else Arrays.fill(dupArr2, arr2.length, maxLength, fill);

        Arrays.setAll(result, i -> dupArr1[i] | dupArr2[i]);

        return result;
    }
}
