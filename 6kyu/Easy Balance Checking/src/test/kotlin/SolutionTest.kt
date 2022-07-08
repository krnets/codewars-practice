package solution

import org.junit.jupiter.api.Test
import kotlin.test.*

class EasyBalanceTest {
    private fun testing(book: String, exp: String) {
        val ans = EasyBalance.balance(book)
        assertEquals(exp, ans)
    }

    @Test
    fun basicTest() {

        val b1 = "1000.00!=\n" +
                "125 Market !=:125.45\n" +
                "126 Hardware =34.95\n" +
                "127 Video! 7.45\n" +
                "128 Book :14.32\n" +
                "129 Gasoline ::16.10\n"

        val b1sol = "Original Balance: 1000.00\\r\\n" +
                "125 Market 125.45 Balance 874.55\\r\\n" +
                "126 Hardware 34.95 Balance 839.60\\r\\n" +
                "127 Video 7.45 Balance 832.15\\r\\n" +
                "128 Book 14.32 Balance 817.83\\r\\n" +
                "129 Gasoline 16.10 Balance 801.73\\r\\n" +
                "Total expense  198.27\\r\\n" +
                "Average expense  39.65"

        val b2 = "1233.00\n" +
                "125 Hardware;! 24.80?\n" +
                "123 Flowers 93.50;\n" +
                "127 Meat 120.90\n" +
                "120 Picture 34.00\n" +
                "124 Gasoline 11.00\n" +
                "123 Photos;! 71.40?\n" +
                "122 Picture 93.50\n" +
                "132 Tyres;! 19.00,?;\n" +
                "129 Stamps; 13.60\n" +
                "129 Fruits{} 17.60\n" +
                "129 Market;! 128.00?\n" +
                "121 Gasoline;! 13.60?"

        val b2sol = "Original Balance: 1233.00\\r\\n" +
                "125 Hardware 24.80 Balance 1208.20\\r\\n" +
                "123 Flowers 93.50 Balance 1114.70\\r\\n" +
                "127 Meat 120.90 Balance 993.80\\r\\n" +
                "120 Picture 34.00 Balance 959.80\\r\\n" +
                "124 Gasoline 11.00 Balance 948.80\\r\\n" +
                "123 Photos 71.40 Balance 877.40\\r\\n" +
                "122 Picture 93.50 Balance 783.90\\r\\n" +
                "132 Tyres 19.00 Balance 764.90\\r\\n" +
                "129 Stamps 13.60 Balance 751.30\\r\\n" +
                "129 Fruits 17.60 Balance 733.70\\r\\n" +
                "129 Market 128.00 Balance 605.70\\r\\n" +
                "121 Gasoline 13.60 Balance 592.10\\r\\n" +
                "Total expense  640.90\\r\\n" +
                "Average expense  53.41"

        testing(b1, b1sol)
        testing(b2, b2sol)
    }
}
