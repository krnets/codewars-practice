public class Solution
{
    public static string solve(string time)
    {
        var arr = new[]
        {
            "o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
            "twelve", "thirteen", "fourteen", "", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
            "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine"
        };

        var quarters = new[] {"", "quarter past", "half past", "quarter to"};
        var HH = int.Parse(time[..2]);
        var hour = HH == 12 ? HH : HH % 12;
        var min = int.Parse(time[3..]);

        return hour == 0 && min == 0 ? 
                    "midnight" : 

            min > 0 && min % 15 == 0 ? 
                    $"{quarters[min / 15]} {(HH == 23 && min > 30 || HH == 0 && min < 30 ? "midnight" : arr[hour + (min > 30 ? 1 : 0)])}" : 

            min == 0 ? 
                    $"{arr[hour]} {arr[min]}" : 

                    hour == 0 ? min > 30 ? 
                            $"{arr[60 - min]} minute{((60 - min) == 1 ? "" : "s")} to one" : 
                            $"{arr[min]} minute{(min == 1 ? "" : "s")} past midnight" : 

                        min > 30 ? 
                            $"{arr[60 - min]} minute{(60 - min == 1 ? "" : "s")} to {(HH == 23 ? "midnight" : arr[hour % 12 + 1])}" : 
                            $"{arr[min]} minute{(min == 1 ? "" : "s")} past {arr[hour]}";
    }
}