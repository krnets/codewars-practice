// 7kyu - Discover The Original Price

// function discoverOriginalPrice(discountedPrice, salePercentage) {
//     let fullPrice = 100 / ((100 - salePercentage) / discountedPrice)

//     return +fullPrice.toFixed(2)
// }

// const discoverOriginalPrice = (discountedPrice, salePercentage) => +(100 / ((100 - salePercentage) / discountedPrice)).toFixed(2)
// const discoverOriginalPrice = (discountedPrice, salePercentage) => +(discountedPrice * 100 / (100 - salePercentage)).toFixed(2)
const discoverOriginalPrice = (discountedPrice, salePercentage) => +(discountedPrice / (1 - salePercentage / 100)).toFixed(2)


// q = discoverOriginalPrice(75,25) // 100
// q
// q = discoverOriginalPrice(25,75) // 100
// q
q = discoverOriginalPrice(75.75, 25) // 101
q