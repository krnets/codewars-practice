package com.codewars.geoffp

import org.junit.Test
import org.junit.Assert.*

class UnwantedDollarsTest {
    @Test
    fun moneyValue() {
        assertEquals(-2.3456, UnwantedDollars.moneyValue("$-2.3456"), 1e-9)
        assertEquals(12.34, UnwantedDollars.moneyValue("12.34"), 1e-9)
        assertEquals(5.67, UnwantedDollars.moneyValue(" $5.67"), 1e-9)
        assertEquals(-0.89, UnwantedDollars.moneyValue("-0.89"), 1e-9)
        assertEquals(-0.10, UnwantedDollars.moneyValue("-$ 0.1"), 1e-9)
        assertEquals(7.0, UnwantedDollars.moneyValue("007"), 1e-9)
        assertEquals(89.0, UnwantedDollars.moneyValue(" $ 89"), 1e-9)
        assertEquals(0.11, UnwantedDollars.moneyValue("   .11"), 1e-9)
        assertEquals(0.20, UnwantedDollars.moneyValue("$.2"), 1e-9)
        assertEquals(-0.34, UnwantedDollars.moneyValue("-.34"), 1e-9)
        assertEquals(0.0, UnwantedDollars.moneyValue("$$$"), 1e-9)
    }
}