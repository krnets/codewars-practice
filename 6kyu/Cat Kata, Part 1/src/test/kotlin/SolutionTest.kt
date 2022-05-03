package catKataPartOne

import kotlin.test.assertEquals
import org.junit.Test

class PeacefulYardTest {
    @Test
    fun ExampleTest1() {
        println("Only one cat is in the yard")
        assertEquals(
            true,
            peacefulYard(
                arrayOf(
                    "------------",
                    "------------",
                    "-L----------",
                    "------------",
                    "------------",
                    "------------"
                ), 10
            )
        );
    }

    @Test
    fun ExampleTest2() {
        println("There are two cats in the yard, and they are closer than the minimum distance")
        assertEquals(
            false,
            peacefulYard(
                arrayOf(
                    "------------",
                    "---M--------",
                    "------------",
                    "------------",
                    "-------R----",
                    "------------"
                ), 6
            )
        );
        println("All three cats are in the yard, all further apart than or equal to the minimum distance")
    }

    @Test
    fun ExampleTest3() {
        assertEquals(
            true,
            peacefulYard(
                arrayOf(
                    "-----------L",
                    "--R---------",
                    "------------",
                    "------------",
                    "------------",
                    "--M---------"
                ), 4
            )
        );
    }

    @Test
    fun ExampleTest4() {
        assertEquals(
            false,
            peacefulYard(
                arrayOf(
                    "------------------M-",
                    "--------------------",
                    "--------------------",
                    "----------------R---",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------"
                ), 11
            )
        );
    }

    @Test
    fun ExampleTest5() {
        assertEquals(
            false,
            peacefulYard(
                arrayOf(
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "---M----------------",
                    "--------------------",
                    "--------------------",
                    "------R---------L---",
                    "--------------------"
                ), 15
            )
        );
    }

    @Test
    fun ExampleTest6() {
        assertEquals(
            true,
            peacefulYard(
                arrayOf(
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------",
                    "--------------------"
                ), 2
            )
        );
    }
}
