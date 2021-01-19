/*public class BouncingBall
{
    public static int bouncingBall(double h, double bounce, double window)
    {
        if (h < 1 || bounce <= 0 || h <= window || bounce >= 1) return -1;

        int times = 1;
        while ((h * bounce) > window)
        {
            h *= bounce;
            times += 2;
        }

        return times;
    }
}*/

public class BouncingBall
{
    public static int bouncingBall(double h, double bounce, double window)
    {
        if (h <= window || bounce <= 0 || bounce >= 1) return -1;

        return 2 + bouncingBall(h * bounce, bounce, window);
    }
}