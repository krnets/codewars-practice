/*
You are given a sequence of a journey in London, UK.
The sequence will contain bus numbers and TFL tube names as strings e.g.

        new Object[] {"Northern", "Central", 243, 1, "Victoria"}

Journeys will always only contain a combination of tube names and bus numbers.
Each tube journey costs £2.40 and each bus journey costs £1.50.
If there are 2 or more adjacent bus journeys, the bus fare is capped for sets of two adjacent
buses and calculated as one bus fare for each set.

Your task is to calculate the total cost of the journey and return the cost
rounded to 2 decimal places in the format (where x is a number): £x.xx
*/

public class Kata {
    public static String londonCityHacker(Object[] journey) {
        var totalCost = 0.0;
        for (int i = 0; i < journey.length; i++) {
            if (journey[i] instanceof String)
                totalCost += 2.4;
            else {
                totalCost += 1.5;
                if (i + 1 < journey.length && journey[i + 1] instanceof Number) {
                    i++;
                }
            }
        }
        return String.format("£%.2f", totalCost);
    }
}