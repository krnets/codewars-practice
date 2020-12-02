/*
public class Xbonacci {
    public double[] tribonacci(double[] s, int n) {
        var sequence = new double[n];
        System.arraycopy(s, 0, sequence, 0, Math.min(n, s.length));

        for (int i = 3; i < n; i++) {
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3];
        }
        return sequence;
    }
}*/

/*
import java.util.Arrays;

public class Xbonacci {
    public double[] tribonacci(double[] s, int n) {
        var sequence = Arrays.copyOf(s, n);
        for (int i = 3; i < n; i++) {
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3];
        }
        return sequence;
    }
}
*/

/*
public class Xbonacci {
    public double[] tribonacci(double[] s, int n) {
        var res = new double[n];
        for (int i = 0; i < n; i++) {
            if (i < 3) res[i] = s[i];
            else res[i] = res[i - 3] + res[i - 2] + res[i - 1];
        }
        return res;
    }
}
*/

import java.util.stream.Stream;

public class Xbonacci {
    public double[] tribonacci(double[] s, int n) {
        return Stream.iterate(s, t -> new double[]{t[1], t[2], t[0] + t[1] + t[2]})
                .limit(n)
                .mapToDouble(t -> t[0])
                .toArray();
    }
}
