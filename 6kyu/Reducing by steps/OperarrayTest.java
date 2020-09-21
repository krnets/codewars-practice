import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.function.LongBinaryOperator;

import org.junit.Test;

public class OperarrayTest {
    private static long gcdi21(long x, long y) {
        x = Math.abs(x);
        y = Math.abs(y);
        while (y != 0) {
            long tmp = x;
            x = y;
            y = tmp % y;
        }
        return x;
    }

    private static long lcmu21(long a, long b) {
        return Math.abs(a * b) / gcdi21(a, b);
    }

    private static long som21(long a, long b) {
        return a + b;
    }

    private static long maxi21(long a, long b) {
        return Math.max(a, b);
    }

    private static long oper21(LongBinaryOperator operator, long a, long b) {
        return ((LongBinaryOperator) operator).applyAsLong(a, b);
    }

    private static long[] operArray21(LongBinaryOperator operator, long[] arr, long init) {
        long c = init;
        long[] res = new long[arr.length];
        for (int i = 0; i < arr.length; i++) {
            c = oper21(operator, c, arr[i]);
            res[i] = c;
        }
        return res;
    }

    //.................
    private static void testing(String actual, String expected) {
        assertEquals(expected, actual);
    }

    private static long randInt(int min, int max) {
        return (long) (min + Math.random() * ((max - min) + 1));
    }

    @Test
    public void test0() {
        System.out.println("Fixed Tests operArray : gcdi, lcmu, som, mini, maxi");
        long[] a = new long[]{18, 69, -90, -78, 65, 40};
        long[] r = new long[]{18, 3, 3, 3, 1, 1};
        testing(Arrays.toString(Operarray.operArray(Operarray::gcdi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{18, 414, 2070, 26910, 26910, 107640};
        testing(Arrays.toString(Operarray.operArray(Operarray::lcmu, a, a[0])),
                Arrays.toString(r));
        r = new long[]{18, 87, -3, -81, -16, 24};
        testing(Arrays.toString(Operarray.operArray(Operarray::som, a, 0)),
                Arrays.toString(r));
        r = new long[]{18, 18, -90, -90, -90, -90};
        testing(Arrays.toString(Operarray.operArray(Operarray::mini, a, a[0])),
                Arrays.toString(r));
        r = new long[]{18, 69, 69, 69, 69, 69};
        testing(Arrays.toString(Operarray.operArray(Operarray::maxi, a, a[0])),
                Arrays.toString(r));
    }

    @Test
    public void test1() {
        long[] a = new long[]{10, 70, -97, -84, -96, -16};
        long[] r = new long[]{10, 10, 1, 1, 1, 1};
        System.out.println("1st series Fixed Tests operArray :  : gcdi, lcmu, som, maxi, mini");
        testing(Arrays.toString(Operarray.operArray(Operarray::gcdi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{10, 70, 6790, 40740, 325920, 325920};
        //System.out.println("1st series Fixed Tests operArray : lcmu");
        testing(Arrays.toString(Operarray.operArray(Operarray::lcmu, a, a[0])),
                Arrays.toString(r));
        r = new long[]{10, 80, -17, -101, -197, -213};
        //System.out.println("1st series Fixed Tests operArray : som");
        testing(Arrays.toString(Operarray.operArray(Operarray::som, a, 0)),
                Arrays.toString(r));
        r = new long[]{10, 70, 70, 70, 70, 70};
        //System.out.println("1st series Fixed Tests operArray : maxi");
        testing(Arrays.toString(Operarray.operArray(Operarray::maxi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{10, 10, -97, -97, -97, -97};
        //System.out.println("1st series Fixed Tests operArray : mini");
        testing(Arrays.toString(Operarray.operArray(Operarray::mini, a, a[0])),
                Arrays.toString(r));
    }

    @Test
    public void test2() {
        long[] a = new long[]{-73, -79, 19, -15, 99, 84};
        long[] r = new long[]{73, 1, 1, 1, 1, 1};
        System.out.println("2nd series Fixed Tests operArray :  : gcdi, lcmu, som, maxi, mini");
        testing(Arrays.toString(Operarray.operArray(Operarray::gcdi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{73, 5767, 109573, 1643595, 54238635, 1518681780};
        //System.out.println("2nd series Fixed Tests operArray : lcmu");
        testing(Arrays.toString(Operarray.operArray(Operarray::lcmu, a, a[0])),
                Arrays.toString(r));
        r = new long[]{-73, -152, -133, -148, -49, 35};
        //System.out.println("2nd series Fixed Tests operArray : som");
        testing(Arrays.toString(Operarray.operArray(Operarray::som, a, 0)),
                Arrays.toString(r));
        r = new long[]{-73, -73, 19, 19, 99, 99};
        //System.out.println("2nd series Fixed Tests operArray : maxi");
        testing(Arrays.toString(Operarray.operArray(Operarray::maxi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{-73, -79, -79, -79, -79, -79};
        //System.out.println("2nd series Fixed Tests operArray : mini");
        testing(Arrays.toString(Operarray.operArray(Operarray::mini, a, a[0])),
                Arrays.toString(r));
    }

    @Test
    public void test3() {
        long[] a = new long[]{-41, 88, 72, 45, 46, 72};
        long[] r = new long[]{41, 1, 1, 1, 1, 1};
        System.out.println("3rd series Fixed Tests operArray : gcdi, lcmu, som, maxi, mini");
        testing(Arrays.toString(Operarray.operArray(Operarray::gcdi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{41, 3608, 32472, 162360, 3734280, 3734280};
        //System.out.println("3rd series Fixed Tests operArray : lcmu");
        testing(Arrays.toString(Operarray.operArray(Operarray::lcmu, a, a[0])),
                Arrays.toString(r));
        r = new long[]{-41, 47, 119, 164, 210, 282};
        //System.out.println("3rd series Fixed Tests operArray : som");
        testing(Arrays.toString(Operarray.operArray(Operarray::som, a, 0)),
                Arrays.toString(r));
        r = new long[]{-41, 88, 88, 88, 88, 88};
        //System.out.println("3rd series Fixed Tests operArray : maxi");
        testing(Arrays.toString(Operarray.operArray(Operarray::maxi, a, a[0])),
                Arrays.toString(r));
        r = new long[]{-41, -41, -41, -41, -41, -41};
        //System.out.println("3rd series Fixed Tests operArray : mini");
        testing(Arrays.toString(Operarray.operArray(Operarray::mini, a, a[0])),
                Arrays.toString(r));
    }

    private static long[] doEx(long k) {
        int i = 0;
        long[] res = new long[(int) k];
        long u = randInt(2, 7);
        while (i < k) {
            if (randInt(0, 5) <= 3)
                res[i] = randInt(1, 40) * u;
            else
                res[i] = -randInt(1, 60);
            i++;
        }
        return res;
    }

    @Test
    public void test4() {
//        System.out.println("Random Tests **** som");
        for (int i = 0; i < 100; i++) {
            long[] v = doEx(randInt(4, 10));
//            System.out.println("Input \n" + Arrays.toString(v));
            testing(Arrays.toString(Operarray.operArray(Operarray::som, v, 0)),
                    Arrays.toString(operArray21(OperarrayTest::som21, v, 0)));
        }
    }

    @Test
    public void test5() {
        System.out.println("Random Tests **** max");
        for (int i = 0; i < 100; i++) {
            long[] v = doEx(randInt(4, 10));
//            System.out.println("Input \n" + Arrays.toString(v));
            testing(Arrays.toString(Operarray.operArray(Operarray::maxi, v, v[0])),
                    Arrays.toString(operArray21(OperarrayTest::maxi21, v, v[0])));

        }
    }

    @Test
    public void test6() {
        System.out.println("Random Tests **** gcdi");
        for (int i = 0; i < 100; i++) {
            long[] v = doEx(randInt(4, 6));
//            System.out.println("Input \n" + Arrays.toString(v));
//            System.out.println("Output \n" + Arrays.toString(operArray21(OperarrayTest::gcdi21, v, v[0])));
            testing(Arrays.toString(Operarray.operArray(Operarray::gcdi, v, v[0])),
                    Arrays.toString(operArray21(OperarrayTest::gcdi21, v, v[0])));

        }
    }

    @Test
    public void test7() {
        System.out.println("Random Tests **** lcmu");
        for (int i = 0; i < 100; i++) {
            long[] v = doEx(4);
//            System.out.println("Input \n" + Arrays.toString(v));
//            System.out.println("Output \n" + Arrays.toString(operArray21(OperarrayTest::lcmu21, v, v[0])));
            testing(Arrays.toString(Operarray.operArray(Operarray::lcmu, v, v[0])),
                    Arrays.toString(operArray21(OperarrayTest::lcmu21, v, v[0])));

        }
    }
}
