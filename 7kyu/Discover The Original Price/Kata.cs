using System;

public static class Kata
{
    public static decimal DiscoverOriginalPrice(decimal discountedPrice, decimal salePercentage)
    {
        return Math.Round(discountedPrice / (1 - salePercentage / 100), 2);
        // return Math.Round(100 / ((100 - salePercentage) / discountedPrice), 2);
    }
}