/*
You are given a list of cogs in a gear train

Each element represents the number of teeth of that cog

        e.g. [100, 50, 25] means

        1st cog has 100 teeth
        2nd cog has 50 teeth
        3rd cog has 25 teeth

If the nth cog rotates clockwise at 1 RPM
what is the RPM of the cogs at each end of the gear train?

Notes
        no two cogs share the same shaft
        return an array whose two elements are RPM of the first and last cogs respectively
        use negative numbers for anti-clockwise rotation
        for convenience n is zero-based
*/


/*
public class Dinglemouse {
    public static double[] cogRpm(final int[] cogs, final int n) {
        var a = cogs[n] *
                (n % 2 == 0 ? 1d : -1d) /
                cogs[0];

        var b = cogs[n] *
                ((cogs.length - 1 - n) % 2 == 0 ? 1d : -1d) /
                cogs[cogs.length - 1];

        return new double[]{a, b};
    }
}
*/

public class Dinglemouse {
    public static double[] cogRpm(final int[] cogs, final int n) {
        int nGears = cogs.length - 1;
        double[] clockwiseRotation = {1d, -1d};
        double firstCogRpm = cogs[n] * clockwiseRotation[n % 2] / cogs[0];
        double lastCogRpm = cogs[n] * clockwiseRotation[(nGears - n) % 2] / cogs[nGears];

        return new double[]{firstCogRpm, lastCogRpm};
    }
}

