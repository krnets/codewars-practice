package mix

import org.junit.jupiter.api.Test
import kotlin.test.*

class mixinMainTest {
    @Test
    fun test1() {
        assertEquals(
            "2:eeeee/2:yy/=:hh/=:rr",
            mix("Are they here", "yes, they are here")
        )
    }

    @Test
    fun test2() {
        assertEquals(
            "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg",
            mix("looping is fun but dangerous", "less dangerous than coding")
        )
    }

    @Test
    fun test3() {
        assertEquals(
            "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss",
            mix("my&friend&Paul has heavy hats! &", "my friend John has many many friends &")
        )
    }

    @Test
    fun test4() {
        assertEquals(
            "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss",
            mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "my frie n d Joh n has ma n y ma n y frie n ds n&")
        )
    }

    @Test
    fun test5() {
        assertEquals(
            "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh",
            mix("Are the kids at home? aaaaa fffff", "Yes they are here! aaaaa fffff")
        )
    }
}