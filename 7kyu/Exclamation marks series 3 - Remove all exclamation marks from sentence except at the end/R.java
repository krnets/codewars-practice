/*
Remove all exclamation marks from the end of words. Words are separated by spaces in the sentence.

        remove("Hi!") === "Hi"
        remove("Hi!!!") === "Hi"
        remove("!Hi") === "!Hi"
        remove("!Hi!") === "!Hi"
        remove("Hi! Hi!") === "Hi Hi"
        remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"
*/

public class R {
    public static String removeBang(String str) {
        return str.replaceAll("\\b!+", "");
    }
}