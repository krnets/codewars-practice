/*
Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3,
the cube above will have volume of (n-1)^3 and so on
until the top which will have a volume of 1^3.

You are given the total volume m of the building.
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m
and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m
if such a n exists or -1 if there is no such n.

Examples:

        findNb(1071225) --> 45
        findNb(91716553919377) --> -1
*/

public class ASum {
    public static long findNb(long m) {
        long cubeSize = 0, n = 1;

        while (cubeSize < m) {
            cubeSize += n * n * n;
            n++;
        }
        return cubeSize == m ? n - 1 : -1;
    }
}

/*
public class ASum {
    public static long findNb(long m) {
        long n = 0;
        while (m > 0)
            m -= ++n * n * n;
        return m == 0 ? n : -1;
    }
}
*/

/*
public class ASum {
    public static long findNb(long m) {
        long n = 0;
        while ((m -= ++n * n * n) > 0);
        return m == 0 ? n : -1;
    }
}*/
