/*
If you have completed the Tribonacci sequence kata, you would know by now that mister
Fibonacci has at least a bigger brother.
If not, give it a quick look to get how things work.

Well, time to expand the family a little more:

Think of a Quadribonacci starting with a signature of 4 elements and each following element
is the sum of the 4 previous,

a Pentabonacci with a signature of 5 elements and each following element is the sum of the 5 previous,
and so on.

Build a Xbonacci function that takes a signature of X elements
each next element is the sum of the last X elements
returns the first n elements of the so seeded sequence.

        xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}
        xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}
        xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}
        xbonacci {1,1} produces the Fibonacci sequence
*/


/*
import java.util.Arrays;

public class Xbonacci {
    public double[] xbonacci(double[] signature, int n) {
        double[] seq = Arrays.copyOf(signature, n);
        int Xlength = signature.length;

        for (int i = Xlength; i < n; i++)
            seq[i] = Arrays.stream(seq, i - Xlength, seq.length).sum();

        return seq;
    }
}
*/

/*
import java.util.Arrays;

public class Xbonacci {
    public double[] xbonacci(double[] signature, int n) {
        int Xlength = signature.length;
        double[] seq = Arrays.copyOf(signature, n);

        for (int i = Xlength; i < n; i++) {
            for (int j = i; j >= i - Xlength; j--) {
                seq[i] += seq[j];
            }
        }
        return seq;
    }
}
*/

import java.util.Arrays;
import java.util.stream.DoubleStream;

public class Xbonacci {
    public double[] xbonacci(double[] signature, int n) {
        int x = signature.length;
        var seq = Arrays.copyOf(signature, n);

        for (int i = x; i < n; i++) {
            var lastXelems = Arrays.copyOfRange(seq, i - x, i);
            seq[i] = DoubleStream.of(lastXelems).sum();
        }
        return seq;
    }
}
