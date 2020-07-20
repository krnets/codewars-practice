/*
Now that the competition gets tough it will Sort out the men from the boys .
Men are the Even numbers and Boys are the odd

Task: Given an array/list [] of n integers,
Separate The even numbers from the odds, or Separate the men from the boys
Notes: Return an array/list where Even numbers come first then odds
Since, Men are stronger than Boys, Then Even numbers in ascending order While odds in descending .

Array/list size is at least *4***
Array/list numbers could be a mixture of positives , negatives
Have no fear , It is guaranteed that no Zeroes will exists

Repetition of numbers in the array/list could occur , So (duplications are not included when separating).

        Input >> Output Examples:

        menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3})
        Explanation:
        Since , { 14 } is the even number here , So it came first , then the odds in descending order {17 , 7 , 3} .

        menFromBoys ({-94, -99 , -100 , -99 , -96 , -99 }) ==> return ({-100 , -96 , -94 , -99})
        Explanation:
        Since , { -100, -96 , -94 } is the even numbers here , So it came first in ascending order , *then** *the odds in descending order { -99 }
        Since , (Duplications are not included when separating) , then you can see only one (-99) was appeared in the final array/list .

        menFromBoys ({49 , 818 , -282 , 900 , 928 , 281 , -282 , -1 }) ==> return ({-282 , 818 , 900 , 928 , 281 , 49 , -1})
        Explanation:
        Since , {-282 , 818 , 900 , 928 } is the even numbers here , So it came first in ascending order , then the odds in descending order { 281 , 49 , -1 }
        Since , (Duplications are not included when separating) , then you can see only one (-282) was appeared in the final array/list .
*/

/*
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.IntStream;

public class Kata {
    public static int[] menFromBoys(final int[] values) {
        int[] men = IntStream.of(values)
                .filter(n -> n % 2 == 0)
                .sorted().toArray();
        int[] boys = IntStream.of(values)
                .filter(n -> n % 2 != 0)
                .boxed()
                .sorted(Collections.reverseOrder())
                .mapToInt(i -> i)
                .toArray();

        int[] both = Arrays.copyOf(men, men.length + boys.length);
        System.arraycopy(boys, 0, both, men.length, boys.length);
        return IntStream.of(both).distinct().toArray();
    }
}*/

/*
import java.util.Arrays;
import java.util.Comparator;

public class Kata {
    public static int[] menFromBoys(final int[] values) {
        return Arrays.stream(values)
                .distinct()
                .boxed()
                .sorted(Comparator.comparing(i -> i % 2 == 0 ? i : -i))
                .sorted(Comparator.comparing(i -> Math.abs(i % 2)))
//                .mapToInt(i -> i)
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
*/

import java.util.Collections;
import java.util.stream.IntStream;

public class Kata {
    public static int[] menFromBoys(final int[] values) {
        var men = IntStream.of(values).filter(i -> i % 2 == 0).sorted();
        var boys = IntStream.of(values).filter(i -> i % 2 != 0).boxed().sorted(Collections.reverseOrder()).mapToInt(i -> i);
        return IntStream.concat(men, boys).distinct().toArray();
    }
}
