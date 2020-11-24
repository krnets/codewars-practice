import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class SortArrayTests {

    @Test
    public void intArrayTests() {
        int[] ai = {1, 2, 3};
        int[] uai = {2, 3, 1};

        assertEquals(ai[0], SortArray.sortArray(uai)[0]);
        assertEquals(ai[1], SortArray.sortArray(uai)[1]);
        assertEquals(ai[2], SortArray.sortArray(uai)[2]);
    }

    @Test
    public void objectTests() {
        Integer[] a = {1, 2, 3};
        Integer[] ua = {2, 3, 1};
        assertArrayEquals(a, SortArray.sortArray(ua));
    }


    @Test
    public void longArrayTests() {
        long[] ai = {1, 2, 3};
        long[] uai = {2, 3, 1};
        assertArrayEquals(ai, SortArray.sortArray(uai));
    }

    @Test
    public void doubleArrayTests() {
        double[] ai = {1.0, 2.0, 3.0};
        double[] uai = {2.0, 3.0, 1.0};
        assertArrayEquals(ai, SortArray.sortArray(uai), 0.01);
    }

    @Test
    public void floatArrayTests() {
        float[] ai = {1f, 2f, 3f};
        float[] uai = {2f, 3f, 1f};
        assertArrayEquals(ai, SortArray.sortArray(uai), 0.01f);
    }

    @Test
    public void stringArrayTests() {
        String[] ai = {"hola1", "hola2", "hola3"};
        String[] uai = {"hola2", "hola3", "hola1"};
        assertArrayEquals(ai, SortArray.sortArray(uai));
    }

}