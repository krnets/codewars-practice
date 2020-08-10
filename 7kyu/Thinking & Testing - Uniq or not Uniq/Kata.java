import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;


/*
public class Kata {
    public static int[] testit(int[] a, int[] b) {
        var aUniq = Arrays.stream(a).distinct().toArray();
        var bUniq = Arrays.stream(b).distinct().toArray();
        var combined = new ArrayList<Integer>();
        for (int value : aUniq) combined.add(value);
        for (int value : bUniq) combined.add(value);
        return combined.stream().sorted().mapToInt(i -> i).toArray();
    }
}*/

/*
public class Kata {
    public static int[] testit(int[] a, int[] b) {
        var aUniq = IntStream.of(a).distinct();
        var bUniq = IntStream.of(b).distinct();
        return IntStream.concat(aUniq, bUniq).sorted().toArray();
    }
}
*/

import static java.util.Arrays.stream;
import static java.util.stream.IntStream.concat;

public class Kata {
    public static int[] testit(int[] a, int[] b) {
        return concat(stream(a).distinct(), stream(b).distinct()).sorted().toArray();
    }
}
