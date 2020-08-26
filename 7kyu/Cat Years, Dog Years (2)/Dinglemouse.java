/*
I have a cat and a dog which I got as kitten / puppy.
I forget when that was, but I do know their current ages as catYears and dogYears.
Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

NOTES:  Results are truncated whole numbers of "human" years

Cat Years

        15 cat years for first year
        +9 cat years for second year
        +4 cat years for each year after that

Dog Years

        15 dog years for first year
        +9 dog years for second year
        +5 dog years for each year after that
*/

public class Dinglemouse {
    public static int[] ownedCatAndDog(final int catYears, final int dogYears) {
        return new int[]{getAge(catYears, 4), getAge(dogYears, 5)};
    }

    private static int getAge(int years, int i) {
        if (years < 15) return 0;
        if (years < 24) return 1;
        return 2 + (years - 24) / i;
    }
}