import java.util.Arrays;

/*
Sum all the numbers of the array except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

        { 6, 2, 1, 8, 10 } => 16
        { 1, 1, 11, 2, 3 } => 6

        If array is empty, null or None, or if only 1 Element exists, return 0.
*/
/*
public class Kata {
    public static int sum(int[] numbers) {
        if (numbers == null || numbers.length <= 1)
            return 0;
        int smallest = Integer.MAX_VALUE;
        int largest = Integer.MIN_VALUE;
        for (int num : numbers) {
            if (num < smallest)
                smallest = num;
            if (num > largest)
                largest = num;
        }
        int total = Arrays.stream(numbers).sum();
        return total - largest - smallest;
    }
}*/
public class Kata {
    public static int sum(int[] numbers) {
        if (numbers == null || numbers.length < 2)
            return 0;
        Arrays.sort(numbers);
        return Arrays.stream(numbers).skip(1).limit(numbers.length - 2).sum();
    }
}
