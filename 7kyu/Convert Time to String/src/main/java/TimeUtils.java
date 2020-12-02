public class TimeUtils {
    public static String convertTime(int timeDiff) {
        int secondsInMinute = 60;
        int minutesInHour = 60;
        int hoursInDay = 24;

        int secondsInHour = secondsInMinute * minutesInHour;
        int secondsInDay = secondsInHour * hoursInDay;

        int days = timeDiff / secondsInDay;
        int hours = timeDiff / secondsInHour % hoursInDay;
        int minutes = timeDiff / secondsInMinute % minutesInHour;
        int seconds = timeDiff % secondsInMinute;

        return String.format("%d %d %d %d", days, hours, minutes, seconds);
    }
}