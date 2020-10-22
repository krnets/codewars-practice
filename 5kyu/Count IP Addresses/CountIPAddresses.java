/*
Implement a function that receives two IPv4 addresses,
and returns the number of addresses between them
(including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings.
The last address will always be greater than the first one.

Examples

        ips_between("10.0.0.0", "10.0.0.50")  ==   50
        ips_between("10.0.0.0", "10.0.1.0")   ==  256
        ips_between("20.0.0.10", "20.0.1.0")  ==  246
*/

/*
import java.util.Arrays;
import java.util.stream.IntStream;

public class CountIPAddresses {
    public static long ipsBetween(String start, String end) {
        int octets = 4;
        var octetRange = Math.pow(2, 8);

        var ipStart = Arrays.stream(start.split("\\.")).mapToInt(Integer::parseInt).toArray();
        var ipEnd = Arrays.stream(end.split("\\.")).mapToInt(Integer::parseInt).toArray();

        return IntStream.range(0, octets)
                .map(i -> (int) (Math.pow(octetRange, octets - i - 1) * (ipEnd[i] - ipStart[i])))
                .sum();
    }
}
*/

public class CountIPAddresses {
    public static long ipsBetween(String start, String end) {
        long count = 0;
        var ipStart = start.split("\\.");
        var ipEnd = end.split("\\.");

        for (int i = 0; i < 4; i++) {
            count *= 256;
            count += Long.parseLong(ipEnd[i]) - Long.parseLong(ipStart[i]);
        }
        return count;
    }
}
