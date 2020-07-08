/*
public class Kata {
    public static double getVolumeOfCuboid(final double length, final double width, final double height) {
        return length * width * height;
    }
}*/
public class Kata {
    public static double getVolumeOfCuboid(final double length, final double width, final double height) {
        if (length <= 0 || width <= 0 || height <= 0)
            return 0;
        return length * width * height;
    }
}
