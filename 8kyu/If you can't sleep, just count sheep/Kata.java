import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
If you can't sleep, just count sheep!!
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
Input will always be valid, i.e. no negative integers.
*/
/*
class Kata {
    public static String countingSheep(int num) {
        String result = "";
        for (int i = 0; i < num; i++) {
            result += String.valueOf(i + 1) + " sheep...";
        }
        return result;
    }
}*/
/*
class Kata {
    public static String countingSheep(int num) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= num; i++)
            sb.append(i + " sheep...");
        return sb.toString();
    }
}
*/
class Kata {
    public static String countingSheep(int num) {
        return IntStream.rangeClosed(1, num).mapToObj(i -> i + " sheep...").collect(Collectors.joining());
    }
}
