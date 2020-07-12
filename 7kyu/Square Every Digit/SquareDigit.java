import java.util.stream.Collectors;

/*
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out,
because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
*/
/*
public class SquareDigit {
    public int squareDigits(int n) {
        var chars = String.valueOf(n).toCharArray();
        var sb = new StringBuilder();
        for (char c : chars) {
            int v = Integer.parseInt(String.valueOf(c));
            sb.append(v * v);
        }
        return Integer.parseInt(String.valueOf(sb));
    }
}
*/
/*
public class SquareDigit {
    public int squareDigits(int n) {
        return Integer.parseInt(String.valueOf(n)
                .chars()
                .map(v -> Integer.parseInt(String.valueOf((char) v)))
                .map(v -> v * v)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining("")));
    }
}
*/
public class SquareDigit {
    public int squareDigits(int n) {
        return String.valueOf(n).chars()
                .map(v -> (int) Math.pow(v - '0', 2))
                .mapToObj(Integer::toString)
                .collect(Collectors.collectingAndThen(Collectors.joining(), Integer::parseInt));
    }
}