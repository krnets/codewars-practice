import org.junit.Test;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;


public class SolutionTest {

    @Test
    public void basicTests() {
        String[][] config  = {{"Hello, World!",             "Hoo!el,Wrdl l"}, // encode
                {"Hello, World!",             "Hlo ol!el,Wrd"},               // encode
                {"Hello, World!",             "H !e,Wdloollr"},               // encode
                {"H !e,Wdloollr",             "Hello, World!"},               //  decode
                {"",                          ""},                            // encode
                {"",                          ""},                            //  decode
                {"WEAREDISCOVEREDFLEEATONCE", "WECRLTEERDSOEEFEAOCAIVDEN"},   // encode
                {"WECRLTEERDSOEEFEAOCAIVDEN", "WEAREDISCOVEREDFLEEATONCE"},   //  decode
                {"WEAREDISCOVEREDFLEEATONCE", "WIREEEDSEEEACAECVDLTNROFO"},   // encode
                {"WIREEEDSEEEACAECVDLTNROFO", "WEAREDISCOVEREDFLEEATONCE"},   //  decode
                {"WEAREDISCOVEREDFLEEATONCE", "WCLEESOFECAIVDENRDEEAOERT"},   // encode
                {"WECRLTEERDSOEEFEAOCAIVDEN", "WLSADOOTEEECEAEECRFINVEDR"}    //  decode
        };
        int[] rails = {3,2,4,4,3,3,3,3,4,4,5,5};
        for (int i=0 ; i<config.length ; i++) {
            String actual = i%2==0 || i==1
                    ? RailFenceCipher.encode(config[i][0], rails[i])
                    : RailFenceCipher.decode(config[i][0], rails[i]);

            assertEquals(config[i][1], actual);
        }
    }


    /* *****************
     *   RANDOM TESTS
     * *****************/

    private static class Sol {

        private static <T> Stream<T> fencer(int n, Stream<T> str) {
            List<List<T>> rails = IntStream.range(0,n)
                    .mapToObj( r -> new ArrayList<T>() )
                    .collect(Collectors.toList());
            int[] xdx = {0, 1};
            int   x=0, dx=1;
            str.forEachOrdered( t -> {
                rails.get(xdx[x]).add(t);
                if (xdx[x]==n-1 && xdx[dx]>0 || xdx[x]==0 && xdx[dx]<0)
                    xdx[dx] *= -1;
                xdx[x] += xdx[dx];
            });
            return rails.stream().flatMap( lst -> lst.stream() );
        }


        static String encode(String s, int n) {
            return fencer( n, s.chars().mapToObj( c -> ""+(char) c) ).collect(Collectors.joining());
        }


        static String decode(String s, int n) {
            List<Integer> idx = fencer(n, IntStream.range(0,s.length()).boxed()).collect(Collectors.toList());
            char[] arr = new char[s.length()];
            int j=0;
            for (char c: s.toCharArray()) arr[ idx.get(j++) ] = c;
            return new String(arr);
        }
    }


    private final Random rnd = new Random();

    private int rand(int start, int end) { return start + rnd.nextInt(end-start); }

    @Test
    public void fixedString_variousRails() {
        String msg = "WEAREDISCOVEREDFLEEATONCE";
        System.out.println("Input for these tests:\n" + msg);

        for (int r=0 ; r<10 ; r++) {
            int rails = rand(2,11);
            String exp = Sol.encode(msg, rails);
            assertEquals(exp, RailFenceCipher.encode(msg, rails));

            rails = rand(2,11);
            exp = Sol.decode(msg, rails);
            assertEquals(exp, RailFenceCipher.decode(msg, rails));
        }
    }

    private static final String lorem = "Amet non facere minima iure unde, provident, "+
            "veritatis officiis asperiores ipsa eveniet sit! Deserunt "+
            "autem excepturi quibusdam iure unde! Porro alias distinctio "+
            "ipsam iure exercitationem molestiae. Voluptate fugiat quasi maiores!jk";
    private static final List<String> lorarr = Arrays.asList(lorem.split(" "));

    @Test
    public void randomTests() {
        System.out.println("Base string for these tests (or a shuffled version):\n" + lorem);

        for (int r=0 ; r<50 ; r++) {
            String msg = shuffle();
            int rails = rand(2,51);
            String exp = Sol.encode(msg, rails);
            assertEquals(exp, RailFenceCipher.encode(msg, rails));

            msg = shuffle();
            rails = rand(2,51);
            exp = Sol.decode(msg, rails);
            assertEquals(exp, RailFenceCipher.decode(msg, rails));
        }
    }

    private String shuffle() {
        Collections.shuffle(lorarr);
        return String.join(" ", lorarr);
    }

}
