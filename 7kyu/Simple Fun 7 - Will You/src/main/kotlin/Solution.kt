/*
fun willYou(young: Boolean, beautiful: Boolean, loved: Boolean): Boolean {
    return (young and beautiful and !loved) or
            ((!young or !beautiful) and loved)
}*/

fun willYou(young: Boolean, beautiful: Boolean, loved: Boolean): Boolean {
    return (young and beautiful) != loved
}
