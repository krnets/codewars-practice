using static System.String;

namespace Solution
{
    public class Kata
    {
        public static string DisplayValue(int value)
        {
            const int hour = 60;
            const int day = 24 * hour;
            const int week = 7 * day;
            const int month = 4 * week;

            int minutes = value % 60;
            int hours = (value / hour) % 24;
            int days = (value / day) % 7;
            int weeks = (value / week) % 4;
            int months = value / month;

            return ($"{(months > 0 ? $"{months} month{(months > 1 ? "s" : Empty)}" : Empty)} ".TrimStart() +
                    $"{(weeks > 0 ? $"{weeks} week{(weeks > 1 ? "s" : Empty)}" : Empty)} ".TrimStart() +
                    $"{(days > 0 ? $"{days} day{(days > 1 ? "s" : Empty)}" : Empty)} ".TrimStart() +
                    $"{(hours > 0 ? $"{hours} hour{(hours > 1 ? "s" : Empty)}" : Empty)} ".TrimStart() +
                    $"{(minutes > 0 ? $"{minutes} minute{(minutes > 1 ? "s" : Empty)}" : Empty)}").Trim();
        }
    }
}