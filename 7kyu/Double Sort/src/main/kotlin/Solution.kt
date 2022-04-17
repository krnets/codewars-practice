package com.codewars.a.partridge

object DoubleSort {
    fun dbSort(a: Array<Any>): Array<Any> {
        val numbers = a.filterIsInstance<Int>().sorted()
        val strings = a.filterIsInstance<String>().sorted()

        return (numbers + strings).toTypedArray()
    }
}