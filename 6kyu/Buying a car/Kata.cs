using System;

public class BuyCar
{
    public static int[] nbMonths(int startPriceOld, int startPriceNew, int savingPerMonth, double percentLossByMonth)
    {
        double depreciationOldCar = startPriceOld;
        double depreciationNewCar = startPriceNew;
        double variablePercentLoss = percentLossByMonth / 100;

        int moneySaved = 0;
        int monthsNeeded = 0;

        while ((depreciationOldCar + moneySaved) < depreciationNewCar)
        {
            depreciationOldCar -= (depreciationOldCar * variablePercentLoss);
            depreciationNewCar -= (depreciationNewCar * variablePercentLoss);

            moneySaved += savingPerMonth;
            monthsNeeded++;

            if ((monthsNeeded + 1) % 2 == 0)
            {
                percentLossByMonth += 0.5;
                variablePercentLoss = percentLossByMonth / 100;
            }
        }

        int moneyLeftOver = (int) Math.Round(depreciationOldCar + moneySaved - depreciationNewCar);

        return new int[] {monthsNeeded, moneyLeftOver};
    }
}