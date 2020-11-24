import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class KataTest {

    @Test
    public void testEncrypt1() {
        assertEquals("This is a test!", Kata.encrypt("This is a test!", 0));
    }

    @Test
    public void testEncrypt2() {
        assertEquals("hsi  etTi sats!", Kata.encrypt("This is a test!", 1));
    }

    @Test
    public void testEncrypt3() {
        assertEquals("s eT ashi tist!", Kata.encrypt("This is a test!", 2));
    }

    @Test
    public void testEncrypt4() {
        assertEquals(" Tah itse sits!", Kata.encrypt("This is a test!", 3));
    }

    @Test
    public void testEncrypt5() {
        assertEquals("This is a test!", Kata.encrypt("This is a test!", 4));
    }

    @Test
    public void testEncrypt6() {
        assertEquals("This is a test!", Kata.encrypt("This is a test!", -1));
    }

    @Test
    public void testEncrypt7() {
        assertEquals("hskt svr neetn!Ti aai eyitrsig", Kata.encrypt("This kata is very interesting!", 1));
    }


    @Test
    public void testDecrypt1() {
        assertEquals("This is a test!", Kata.decrypt("This is a test!", 0));
    }

    @Test
    public void testDecrypt2() {
        assertEquals("This is a test!", Kata.decrypt("hsi  etTi sats!", 1));
    }

    @Test
    public void testDecrypt3() {
        assertEquals("This is a test!", Kata.decrypt("s eT ashi tist!", 2));
    }

    @Test
    public void testDecrypt4() {
        assertEquals("This is a test!", Kata.decrypt(" Tah itse sits!", 3));
    }

    @Test
    public void testDecrypt5() {
        assertEquals("This is a test!", Kata.decrypt("This is a test!", 4));
    }

    @Test
    public void testDecrypt6() {
        assertEquals("This is a test!", Kata.decrypt("This is a test!", -1));
    }

    @Test
    public void testDecrypt7() {
        assertEquals("This kata is very interesting!", Kata.decrypt("hskt svr neetn!Ti aai eyitrsig", 1));
    }

    @Test
    public void testNullOrEmpty1() {
        assertEquals("", Kata.encrypt("", 0));
    }

    @Test
    public void testNullOrEmpty2() {
        assertEquals("", Kata.decrypt("", 0));
    }

    @Test
    public void testNullOrEmpty3() {
        assertNull(Kata.encrypt(null, 0));
    }

    @Test
    public void testNullOrEmpty4() {
        assertNull(Kata.decrypt(null, 0));
    }

    @Test
    public void encryptDecryptTests() {
        assertEquals("Kobayashi-Maru-Test", Kata.decrypt(Kata.encrypt("Kobayashi-Maru-Test", 10), 10));
    }
}