/*
Replace the word(s) coverage by covfefe, however, if word covfefe is not in the string,
add covfefe at the end with a leading space.
*/

/*
public class Covfefe {
    public static String covfefe(String tweet) {
        return tweet.contains("coverage") ? tweet.replaceAll("coverage", "covfefe") : tweet + " covfefe";
    }
}*/
public class Covfefe {
    public static String covfefe(String tweet) {
        return tweet.matches(".*coverage.*") ? tweet.replaceAll("coverage", "covfefe") : tweet + " covfefe";
    }
}
