fun fizzBuzz(n: Int): Array<String> = (1..n).map { x ->
    ("Fizz".repeat(if (x % 3 == 0) 1 else 0) + "Buzz".repeat(if (x % 5 == 0) 1 else 0))
        .ifEmpty { x.toString() }
    }.toTypedArray()

/*
fun fizzBuzz(n: Int): Array<String> = (1..n).map { x ->
    when {
        x.mod(15) == 0 -> "FizzBuzz"
        x.mod(5) == 0 -> "Buzz"
        x.mod(3) == 0 -> "Fizz"
        else -> x.toString()
    }
}.toTypedArray()
*/

/*
fun fizzBuzz(n: Int): Array<String> = (1..n).map { x ->
    when {
        x % 15 == 0 -> "FizzBuzz"
        x % 5 == 0 -> "Buzz"
        x % 3 == 0 -> "Fizz"
        else -> "$x"
    }
}.toTypedArray()
*/
