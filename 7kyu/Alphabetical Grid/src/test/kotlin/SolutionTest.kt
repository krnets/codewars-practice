package kata

import org.junit.Test
import kotlin.test.assertEquals

class ExampleTests {
    fun runTest(n: Int, refSol: String?) = assertEquals(refSol, Kata.grid(n))

    @Test
    fun `Valid tests`() {
        runTest(0, "")
        runTest(1, "a")
        runTest(2, "a b\nb c")
        runTest(4, "a b c d\nb c d e\nc d e f\nd e f g")
        runTest(6, "a b c d e f\nb c d e f g\nc d e f g h\nd e f g h i\ne f g h i j\nf g h i j k")
        runTest(
            27,
            "a b c d e f g h i j k l m n o p q r s t u v w x y z a" +
                    "\n" +
                    "b c d e f g h i j k l m n o p q r s t u v w x y z a b" +
                    "\n" +
                    "c d e f g h i j k l m n o p q r s t u v w x y z a b c" +
                    "\n" +
                    "d e f g h i j k l m n o p q r s t u v w x y z a b c d" +
                    "\n" +
                    "e f g h i j k l m n o p q r s t u v w x y z a b c d e" +
                    "\n" +
                    "f g h i j k l m n o p q r s t u v w x y z a b c d e f" +
                    "\n" +
                    "g h i j k l m n o p q r s t u v w x y z a b c d e f g" +
                    "\n" +
                    "h i j k l m n o p q r s t u v w x y z a b c d e f g h" +
                    "\n" +
                    "i j k l m n o p q r s t u v w x y z a b c d e f g h i" +
                    "\n" +
                    "j k l m n o p q r s t u v w x y z a b c d e f g h i j" +
                    "\n" +
                    "k l m n o p q r s t u v w x y z a b c d e f g h i j k" +
                    "\n" +
                    "l m n o p q r s t u v w x y z a b c d e f g h i j k l" +
                    "\n" +
                    "m n o p q r s t u v w x y z a b c d e f g h i j k l m" +
                    "\n" +
                    "n o p q r s t u v w x y z a b c d e f g h i j k l m n" +
                    "\n" +
                    "o p q r s t u v w x y z a b c d e f g h i j k l m n o" +
                    "\n" +
                    "p q r s t u v w x y z a b c d e f g h i j k l m n o p" +
                    "\n" +
                    "q r s t u v w x y z a b c d e f g h i j k l m n o p q" +
                    "\n" +
                    "r s t u v w x y z a b c d e f g h i j k l m n o p q r" +
                    "\n" +
                    "s t u v w x y z a b c d e f g h i j k l m n o p q r s" +
                    "\n" +
                    "t u v w x y z a b c d e f g h i j k l m n o p q r s t" +
                    "\n" +
                    "u v w x y z a b c d e f g h i j k l m n o p q r s t u" +
                    "\n" +
                    "v w x y z a b c d e f g h i j k l m n o p q r s t u v" +
                    "\n" +
                    "w x y z a b c d e f g h i j k l m n o p q r s t u v w" +
                    "\n" +
                    "x y z a b c d e f g h i j k l m n o p q r s t u v w x" +
                    "\n" +
                    "y z a b c d e f g h i j k l m n o p q r s t u v w x y" +
                    "\n" +
                    "z a b c d e f g h i j k l m n o p q r s t u v w x y z" +
                    "\n" +
                    "a b c d e f g h i j k l m n o p q r s t u v w x y z a"
        )
        runTest(
            28,
            "a b c d e f g h i j k l m n o p q r s t u v w x y z a b" +
                    "\n" +
                    "b c d e f g h i j k l m n o p q r s t u v w x y z a b c" +
                    "\n" +
                    "c d e f g h i j k l m n o p q r s t u v w x y z a b c d" +
                    "\n" +
                    "d e f g h i j k l m n o p q r s t u v w x y z a b c d e" +
                    "\n" +
                    "e f g h i j k l m n o p q r s t u v w x y z a b c d e f" +
                    "\n" +
                    "f g h i j k l m n o p q r s t u v w x y z a b c d e f g" +
                    "\n" +
                    "g h i j k l m n o p q r s t u v w x y z a b c d e f g h" +
                    "\n" +
                    "h i j k l m n o p q r s t u v w x y z a b c d e f g h i" +
                    "\n" +
                    "i j k l m n o p q r s t u v w x y z a b c d e f g h i j" +
                    "\n" +
                    "j k l m n o p q r s t u v w x y z a b c d e f g h i j k" +
                    "\n" +
                    "k l m n o p q r s t u v w x y z a b c d e f g h i j k l" +
                    "\n" +
                    "l m n o p q r s t u v w x y z a b c d e f g h i j k l m" +
                    "\n" +
                    "m n o p q r s t u v w x y z a b c d e f g h i j k l m n" +
                    "\n" +
                    "n o p q r s t u v w x y z a b c d e f g h i j k l m n o" +
                    "\n" +
                    "o p q r s t u v w x y z a b c d e f g h i j k l m n o p" +
                    "\n" +
                    "p q r s t u v w x y z a b c d e f g h i j k l m n o p q" +
                    "\n" +
                    "q r s t u v w x y z a b c d e f g h i j k l m n o p q r" +
                    "\n" +
                    "r s t u v w x y z a b c d e f g h i j k l m n o p q r s" +
                    "\n" +
                    "s t u v w x y z a b c d e f g h i j k l m n o p q r s t" +
                    "\n" +
                    "t u v w x y z a b c d e f g h i j k l m n o p q r s t u" +
                    "\n" +
                    "u v w x y z a b c d e f g h i j k l m n o p q r s t u v" +
                    "\n" +
                    "v w x y z a b c d e f g h i j k l m n o p q r s t u v w" +
                    "\n" +
                    "w x y z a b c d e f g h i j k l m n o p q r s t u v w x" +
                    "\n" +
                    "x y z a b c d e f g h i j k l m n o p q r s t u v w x y" +
                    "\n" +
                    "y z a b c d e f g h i j k l m n o p q r s t u v w x y z" +
                    "\n" +
                    "z a b c d e f g h i j k l m n o p q r s t u v w x y z a" +
                    "\n" +
                    "a b c d e f g h i j k l m n o p q r s t u v w x y z a b" +
                    "\n" +
                    "b c d e f g h i j k l m n o p q r s t u v w x y z a b c"
        )
    }

    @Test
    fun `Invalid tests`() {
        runTest(-1, null)
        runTest(-5, null)
    }
}