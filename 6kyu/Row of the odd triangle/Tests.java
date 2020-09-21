import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.assertArrayEquals;

public class Tests {
    @Test
    public void fixed_test_1() {
        assertArrayEquals(new long[]{1}, UserSolution.oddRow(1));
    }

    @Test
    public void fixed_test_2() {
        assertArrayEquals(new long[]{3, 5}, UserSolution.oddRow(2));
    }

    @Test
    public void fixed_test_13() {
        assertArrayEquals(new long[]{
                157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181
        }, UserSolution.oddRow(13));
    }

    @Test
    public void fixed_test_19() {
        assertArrayEquals(new long[]{
                343, 345, 347, 349, 351, 353, 355, 357, 359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379
        }, UserSolution.oddRow(19));
    }

    @Test
    public void fixed_test_41() {
        assertArrayEquals(new long[]{
                1641, 1643, 1645, 1647, 1649, 1651, 1653, 1655, 1657, 1659, 1661, 1663, 1665, 1667, 1669,
                1671, 1673, 1675, 1677, 1679, 1681, 1683, 1685, 1687, 1689, 1691, 1693, 1695, 1697, 1699,
                1701, 1703, 1705, 1707, 1709, 1711, 1713, 1715, 1717, 1719, 1721
        }, UserSolution.oddRow(41));
    }

    @Test
    public void fixed_test_93() {
        assertArrayEquals(new long[]{
                8557, 8559, 8561, 8563, 8565, 8567, 8569, 8571, 8573, 8575, 8577, 8579, 8581, 8583, 8585,
                8587, 8589, 8591, 8593, 8595, 8597, 8599, 8601, 8603, 8605, 8607, 8609, 8611, 8613, 8615,
                8617, 8619, 8621, 8623, 8625, 8627, 8629, 8631, 8633, 8635, 8637, 8639, 8641, 8643, 8645,
                8647, 8649, 8651, 8653, 8655, 8657, 8659, 8661, 8663, 8665, 8667, 8669, 8671, 8673, 8675,
                8677, 8679, 8681, 8683, 8685, 8687, 8689, 8691, 8693, 8695, 8697, 8699, 8701, 8703, 8705,
                8707, 8709, 8711, 8713, 8715, 8717, 8719, 8721, 8723, 8725, 8727, 8729, 8731, 8733, 8735,
                8737, 8739, 8741
        }, UserSolution.oddRow(93));
    }

    @Test
    public void small_random_tests() {
        Random r = new Random();
        for (int i = 0; i < 50; i++) {
            int n = 1 + r.nextInt(50);
            assertArrayEquals(solution(n), UserSolution.oddRow(n));
        }
    }

    @Test
    public void big_random_tests() {
        Random r = new Random();
        for (int i = 0; i < 50; i++) {
            int n = 7000000 + r.nextInt(1000000);
            assertArrayEquals(solution(n), UserSolution.oddRow(n));
        }
    }

    private long[] solution(int n) {
        long m = (n - 1), r[] = new long[n];
        m = m * n + 1;
        for (int i = 0; i < n; i++)
            r[i] = m + i * 2;
        return r;
    }
}