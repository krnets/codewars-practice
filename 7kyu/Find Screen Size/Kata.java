/*
Cheesy Cheeseman just got a new monitor! He is happy with it, but he just discovered that his old desktop wallpaper
no longer fits. He wants to find a new wallpaper, but does not know which size wallpaper he should be looking for,
and alas, he just threw out the new monitor's box. Luckily he remembers the width and the aspect ratio of the monitor
from when Bob Mortimer sold it to him. Can you help Cheesy out?

The Challenge
        Given an integer width and a string ratio written as WIDTH:HEIGHT,
        output the screen dimensions as a string written as WIDTHxHEIGHT.
*/

public class Kata {
    public static String findScreenHeight(int width, String ratio) {
        var ratios = ratio.split(":");
        var height = width * Integer.parseInt(ratios[1]) / Integer.parseInt(ratios[0]);
        return String.format("%dx%d", width, height);
    }
}
