import java.math.BigInteger;
import static java.math.BigInteger.ONE;
import static java.math.BigInteger.valueOf;

public class Diagonal {

    public static BigInteger diagonal(int n, int p) {
        BigInteger sum = ONE, index = ONE, previous = ONE,
                diagonal = valueOf(p),
                end = valueOf(n).subtract(diagonal).add(ONE);

        while (index.compareTo(end) < 0) {
            previous = previous.multiply(diagonal.add(index)).divide(index);
            sum = sum.add(previous);
            index = index.add(ONE);
        }
        return sum;
    }
}