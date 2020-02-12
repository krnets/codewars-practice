// 7kyu - Cat Years, Dog Years (2)

/* I have a cat and a dog which I got as kitten / puppy.
I forget when that was, but I do know their current ages as catYears and dogYears.
Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

    Results are truncated whole numbers of "human" years

Cat Years
    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that

Dog Years
    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that */

// function ownedCatAndDog(catYears, dogYears) {
//     const getAge = (years, a) => (years < 15 ? 0 : years < 24 ? 1 : 2 + (years - 24) / a)
//     return [Math.floor(getAge(catYears, 4)), Math.floor(getAge(dogYears, 5))]
// }

function ownedCatAndDog(catYears, dogYears) {
    return [catYears < 15 ? 0 : catYears < 24 ? 1 : (catYears - 16) / 4 | 0,
            dogYears < 15 ? 0 : dogYears < 24 ? 1 : (dogYears - 14) / 5 | 0]
}

q = ownedCatAndDog(15, 15) // [1,1]
q
q = ownedCatAndDog(24, 24) // [2,2]
q
q = ownedCatAndDog(56, 64) // [10,10]
q
