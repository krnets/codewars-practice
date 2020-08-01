/*
Simple enough this one - you will be given an array.
The values in the array will either be numbers or strings, or a mix of both.
You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order,
followed by the strings sorted in alphabetic order.
The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings.
*/

//package com.codewars.a.partridge;

import java.util.ArrayList;
import java.util.stream.Stream;

/*
public class DoubleSort {
    public static Object[] dbSort(Object[] a) {
        var numbers = new ArrayList<Integer>();
        var strings = new ArrayList<String>();

        for (Object o : a) {
            if (o instanceof String)
                strings.add(String.valueOf(o));
            else
                numbers.add((Integer) o);
        }
        return Stream.concat(numbers.stream().sorted(), strings.stream().sorted())
                .toArray(Object[]::new);
    }
}
*/

public class DoubleSort {
    public static Object[] dbSort(Object[] a) {
        var numbers = Stream.of(a).filter(Integer.class::isInstance).sorted();
        var strings = Stream.of(a).filter(String.class::isInstance).sorted();
        return Stream.concat(numbers, strings).toArray();
    }
}
