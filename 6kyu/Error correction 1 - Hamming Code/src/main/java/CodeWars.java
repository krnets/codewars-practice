import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class CodeWars {
    private final int hammingCodeLength = 3;

    public String encode(String text) {
        String bits = text.chars()
                .mapToObj(c -> Integer.toBinaryString((1 << Byte.SIZE) | c).substring(1))
                .collect(Collectors.joining());

        return bits.chars()
                .mapToObj(Character::toString)
                .map(c -> c.repeat(hammingCodeLength))
                .collect(Collectors.joining());
    }

    public String decode(String bits) {
        String bitsCorrected = Arrays.stream(bits
                .split("(?<=\\G.{" + hammingCodeLength + "})"))
                .map(this::correctBit)
                .collect(Collectors.joining());

        return IntStream.iterate(0, i -> i < bitsCorrected.length(), i -> i + Byte.SIZE)
                .map(i -> Integer.parseInt(bitsCorrected.substring(i, i + Byte.SIZE), 2))
                .mapToObj(Character::toString)
                .collect(Collectors.joining());
    }

    private String correctBit(String slice) {
        return slice.chars()
                .map(Character::getNumericValue)
                .sum() > 1 ? "1" : "0";
    }
}
