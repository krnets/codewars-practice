/*
A number is called Automorphic number if and only if its square ends in the same digits as the number itself.
Task: Given a number determine if it Automorphic or not .
*/

/*
public class Solution {
    public static String autoMorphic(int number) {
        return String.valueOf(number * number).endsWith(String.valueOf(number)) ? "Automorphic" : "Not!!";
    }
}*/

public class Solution {
    public static String autoMorphic(int number) {
        return (number * number + "").endsWith(number + "") ? "Automorphic" : "Not!!";
    }
}
