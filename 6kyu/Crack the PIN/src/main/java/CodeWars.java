import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.stream.IntStream;

public class CodeWars {
    public String crack(String hash) {
        return IntStream.range(1, 100000)
                .mapToObj(i -> String.format("%05d", i))
                .filter(data -> md5Hex(data).equals(hash))
                .findFirst().orElse("");
    }

    private String md5Hex(String data) {
        MessageDigest m = null;
        byte[] digest = new byte[0];
        try {
            m = MessageDigest.getInstance("MD5");
            m.update(data.getBytes());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        digest = m.digest();
        return new BigInteger(1, digest).toString(16);
    }
}
