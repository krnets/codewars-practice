import java.util.stream.IntStream;

/*
import java.util.Arrays;

public class Sum {
    public static int arrayPlusArray(int[] arr1, int[] arr2) {
        return Arrays.stream(arr1).sum() + Arrays.stream(arr2).sum();
    }
}*/
public class Sum {
    public static int arrayPlusArray(int[] arr1, int[] arr2) {
        return IntStream.of(arr1).sum() + IntStream.of(arr2).sum();
    }
}
