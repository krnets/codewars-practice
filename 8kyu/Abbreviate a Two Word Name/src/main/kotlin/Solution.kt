/*
fun abbrevName(name: String): String {
    var (firstName, lastName) = name.split(" ")

    return "${firstName.first().uppercase()}.${lastName.first().uppercase()}"
}*/

fun abbrevName(name: String): String = name.split(" ").joinToString(".") { it.first().uppercase() }
