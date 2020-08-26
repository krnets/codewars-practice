/*
Find the difference between two collections.
The difference means that either the character is present in one collection or it is present in other,
but not in both. Return a sorted set with difference.

The collections can contain any character and can contain duplicates.

For instance:

        A = [a,a,t,e,f,i,j]
        B = [t,g,g,i,k,f]

        difference = [a,e,g,j,k]
*/

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
public class Kata {
    public static List<Character> diff(Collection<Character> a, Collection<Character> b) {
        var setA = new HashSet<>(a);
        var setB = new HashSet<>(b);
        var difference = new ArrayList<Character>();

        for (Character c : setA) {
            if (!setB.contains(c))
                difference.add(c);
        }
        for (Character c : setB) {
            if (!setA.contains(c))
                difference.add(c);
        }
        Collections.sort(difference);

        return difference;
    }
}*/


public class Kata {
    public static List<Character> diff(Collection<Character> a, Collection<Character> b) {
        var ts = new TreeSet<Character>();
        for (var c : a) if (!b.contains(c)) ts.add(c);
        for (var c : b) if (!a.contains(c)) ts.add(c);
        return new ArrayList<>(ts);
    }
}

/*
public class Kata {
    public static List<Character> diff(Collection<Character> a, Collection<Character> b) {
        var setA = new HashSet<>(a);
        var setB = new HashSet<>(b);

        var intersection = new HashSet<>(setA);

        intersection.retainAll(setB);
        var union = new HashSet<>(setA);
        union.addAll(setB);

        // union minus intersection equals symmetric-difference
        var symmetricDifference = new HashSet<>(union);
        symmetricDifference.removeAll(intersection);

        var result = new ArrayList<>(symmetricDifference);
        result.sort(Character::compareTo);

        return result;
    }
}
*/

/*
public class Kata {
    public static List<Character> diff(Collection<Character> a, Collection<Character> b) {
        return Stream.of(a, b)
                .flatMap(Collection::stream)
                .distinct()
                .filter(c -> !a.contains(c) || !b.contains(c))
                .sorted()
                .collect(Collectors.toList());
    }
}

*/
/*
public class Kata {
    public static List<Character> diff(Collection<Character> a, Collection<Character> b) {
        return Stream.concat(a.stream(), b.stream())
                .distinct()
                .filter(c -> !a.contains(c) || !b.contains(c))
                .sorted()
                .collect(Collectors.toList());
    }
}
*/
