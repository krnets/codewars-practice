/*
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.
*/
/*
public class FakeBinary {
    public static String fakeBin(String numberString) {
        return numberString.replaceAll("[1234]", "0").replaceAll("[56789]", "1");
    }
}*/
public class FakeBinary {
    public static String fakeBin(String numberString) {
        return numberString.replaceAll("[1-4]", "0").replaceAll("[5-9]", "1");
    }
}
