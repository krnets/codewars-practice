import java.util.Arrays;

/*
public class Solution {
    public static boolean check(Object[] a, Object x) {
        for (Object o : a)
            if (o == x)
                return true;
        return false;
    }
}*/
public class Solution {
    public static boolean check(Object[] a, Object x) {
        return Arrays.asList(a).contains(x);
    }
}
