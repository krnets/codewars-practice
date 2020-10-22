/*
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

        1st octet 128 has the binary representation: 10000000
        2nd octet 32 has the binary representation: 00100000
        3rd octet 10 has the binary representation: 00001010
        4th octet 1 has the binary representation: 00000001

        So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits,
we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number
and returns a string representation of its IPv4 address.

Examples

        2149583361 ==> "128.32.10.1"
        32         ==> "0.0.0.32"
        0          ==> "0.0.0.0"
*/

/*
import java.util.ArrayList;

public class Kata {
    public static String longToIP(long ip) {
        var binaryString = Long.toBinaryString(ip);
        var padZeros = "0".repeat(Byte.SIZE * 4 - binaryString.length());
        var fullBinaryString = padZeros + binaryString;
        var octets = new ArrayList<String>();

        for (int i = 0; i < fullBinaryString.length(); i += Byte.SIZE) {
            var binarySlice = fullBinaryString.substring(i, i + Byte.SIZE);
            int octet = Integer.parseInt(binarySlice, 2);
            octets.add(String.valueOf(octet));
        }
        return String.join(".", octets);
    }
}
*/

/*
import com.google.common.net.InetAddresses;

public class Kata {
    public static String longToIP(long ip) {
        return InetAddresses.fromInteger((int) ip).getHostAddress();
    }
}*/

public class Kata {
    public static String longToIP(long ip) {
        var octets = new long[4];

        for (int i = 0; i < 4; i++) {
            octets[i] = (ip >>> (i * Byte.SIZE) & 0xFF);
        }
        return String.format("%d.%d.%d.%d", octets[3], octets[2], octets[1], octets[0]);
    }
}
