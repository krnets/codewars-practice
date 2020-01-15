// 6kyu - Aspect Ratio Cropping - Part 2

/* Comparing two different aspect ratios poses some subtleties – when comparing two aspect ratios, 
one may compare images with equal height, equal width, equal diagonal, or equal area.

Write a function that accepts arbitrary X and Y resolutions and converts them into resolutions with a 16:9 aspect ratio. 
This time your function should accept a third input "constant," specifying the variable to remain constant in your conversion. 
The variable constant can have a value of either "height", "width", "diagonal", or "area". 
Round your answers up to the nearest integer. */

// function aspectRatio (x, y, constant) {
//     let ratio = 16 / 9
//     let diag = Math.sqrt(x * x + y * y)
//     let area = x * y
//     switch (constant) {
//         case 'height':   return [Math.ceil(y * ratio), y]
//         case 'width':    return [x, Math.ceil(x / ratio)]
//         case 'area':     return [Math.ceil(Math.sqrt(area * ratio)),Math.ceil(Math.sqrt(area / ratio))]
//         case 'diagonal': return [Math.ceil((ratio * diag) / Math.sqrt(ratio ** 2 + 1)),
//                                  Math.ceil((diag / Math.sqrt(ratio ** 2 + 1)))]
//         default: break
//     }
// }

function aspectRatio (x, y, constant) {
    let aspect = []
    let ratio = 16 / 9
    let diag = Math.sqrt(x * x + y * y)
    let area = x * y
    switch (constant) {
        case 'height':    aspect = [y * ratio, y]; break
        case 'width':     aspect = [x, x / ratio]; break
        case 'area':      aspect = [Math.sqrt(area * ratio), Math.sqrt(area / ratio)]; break
        case 'diagonal':  aspect = [ratio * diag / Math.sqrt(ratio ** 2 + 1), diag / Math.sqrt(ratio ** 2 + 1)]; break
    }
    return aspect.map(Math.ceil)
}


q = aspectRatio(374, 280, "height") // [498 ,280]
q
q = aspectRatio(374, 280, "width") // [374 ,211]
q
q = aspectRatio(374, 280, "diagonal") // [408 ,230]
q
q = aspectRatio(374, 280, "area") // [432 ,243]
q
q = aspectRatio(374, 280, "sum") // []
q