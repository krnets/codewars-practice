/*
Wikipedia: The regular paperfolding sequence, also known as the dragon curve sequence,
is an infinite automatic sequence of 0s and 1s defined as the limit of the following process:

        1
        1 1 0
        1 1 0 1 1 0 0
        1 1 0 1 1 0 0 1 1 1 0 0 1 0 0

At each stage an alternating sequence of 1s and 0s is inserted between the terms of the previous sequence.

Define a generator PaperFold that sequentially generates the values of this sequence.

It will be tested for up to 1 000 000 values.
*/

/*
import java.util.function.IntSupplier;

public class PaperFold implements IntSupplier {
    private static final String SEQUENCE_START = "1";

    private boolean onOne = true;
    private char getNext() {
        return ((onOne = !onOne) ? '0' : '1');

    public int getAsInt() {
        return 1;
    }
}

    String generate(int steps) {
        String sequence = SEQUENCE_START;
        for (int i = 0; i < steps; i++) {
            for (int j = 0; j < sequence.length(); j += 2) {
                sequence = sequence.substring(0, j) + getNext() + sequence.substring(j);
            }
            sequence += getNext();
        }
        return sequence;
    }
*/


/*
    private static final String SEQUENCE_START = "1";

    private boolean onOne = true;

    String generate(int steps) {
        String sequence = SEQUENCE_START;
        for (int i = 0; i < steps; i++) {
            for (int j = 0; j < sequence.length(); j += 2) {
                sequence = sequence.substring(0, j) + getNext() + sequence.substring(j);
            }
            sequence += getNext();
        }
        return sequence;
    }

    private char getNext() {
        return ((onOne = !onOne) ? '0' : '1');
    }

}*/

/*
import java.util.function.IntSupplier;
import java.util.stream.IntStream;

public class PaperFold implements IntSupplier {
    private int i = 0;

    private final int[] seq = IntStream.rangeClosed(1, 1000000)
            .map(i -> ~(i >> Integer.numberOfTrailingZeros(i) + 1) & 1)
            .toArray();

    public int getAsInt() {
        return seq[i++];
    }
}

*/

import java.util.function.IntSupplier;

class PaperFold implements IntSupplier {
    int i = 0;

    public int getAsInt() {
        return (++i & Integer.lowestOneBit(i) << 1) == 0 ? 1 : 0;
    }
}