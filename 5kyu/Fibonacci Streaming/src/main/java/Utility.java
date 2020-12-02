import java.util.stream.IntStream;
import java.util.stream.Stream;

/*
public class Utility {

    public static IntStream generateFibonacciSequence() {
        return Stream.iterate(new int[]{1, 0},
                seq -> new int[]{seq[0] + seq[1], seq[0]})
                .mapToInt(seq -> seq[0]);
    }
}*/

public class Utility {

    public static IntStream generateFibonacciSequence() {
        return Stream.iterate(new int[]{1, 1},
                seq -> new int[]{seq[1], seq[0] + seq[1]})
                .mapToInt(seq -> seq[0]);
    }
}
