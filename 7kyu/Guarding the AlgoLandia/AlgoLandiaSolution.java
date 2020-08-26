/*
In a far away country called AlgoLandia, there are N islands numbered 1 to N.
Each island is denoted by k[i].
King Algolas, king of AlgoLandia, built N - 1 bridges in the country.
A bridge is built between islands k[i] and k[i+1].
Bridges are two-ways and are expensive to build.

The problem is that there are gangs who wants to destroy the bridges.
In order to protect the bridges, the king wants to assign elite guards to the bridges.
A bridge between islands k[i] and k[i+1] is safe when there is an elite guard in island k[i] or k[i+1].
There are already elite guards assigned in some islands.

Your task now is to determine the minimum number of additional elite guards that needs to be hired
to guard all the bridges.

Note:   You are given a sequence k with N length. k[i] = true,
        means that there is an elite guard in that island;
        k[i] = false means no elite guard.
        It is guaranteed that AlgoLandia have at least 2 islands.

        k = [true, true, false, true, false] => 0
        k = [false, false, true, false, false] => 2
*/

/*
import static java.util.regex.Pattern.compile;
import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.range;

public class AlgoLandiaSolution {
    public static int findNeededGuards(boolean[] k) {
        return (int) compile("1{2}")
                .matcher(range(0, k.length)
                        .mapToObj(b -> k[b] ? "0" : "1")
                        .collect(joining()))
                .results()
                .count();
    }
}
*/

public class AlgoLandiaSolution {
    public static int findNeededGuards(boolean[] k) {
        int gap = 0;
        int extraGuards = 0;
        for (boolean guarded : k) {
            gap = !guarded ? gap + 1 : 0;
            if (gap > 1) {
                extraGuards++;
                gap = 0;
            }
        }
        return extraGuards;
    }
}