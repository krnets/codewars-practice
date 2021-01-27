namespace myjinxin
{
    using System;

    public class Kata
    {
        public int GrowingPlant(int UpSpeed, int DownSpeed, int DesiredHeight)
        {
            int days = 0;
            int plantHeight = 0;

            while (plantHeight < DesiredHeight)
            {
                plantHeight += UpSpeed;
                days++;

                if (plantHeight >= DesiredHeight)
                    return days;

                plantHeight -= DownSpeed;
            }

            return days;
        }
    }
}

/*namespace myjinxin
{
    using System;

    public class Kata
    {
        public int GrowingPlant(int UpSpeed, int DownSpeed, int DesiredHeight)
        {
            return 1 + (int) Math.Ceiling(Math.Max((DesiredHeight - UpSpeed) / (double) (UpSpeed - DownSpeed), 0.0));
        }
    }
}*/