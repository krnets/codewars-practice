fun rowSumOddNumbers(n: Int): Int = (n * (n - 1) + 1..Int.MAX_VALUE step 2).take(n).sum()