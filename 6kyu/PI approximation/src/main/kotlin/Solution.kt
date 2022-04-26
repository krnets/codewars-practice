package solution

object PiApprox {
    fun iterPi2String(epsilon: Double): String {
        var i = 1
        var result = 1.0

        while (Math.abs(4 * result - Math.PI) > epsilon) {
            if (i % 2 == 0)
                result += (1.0 / (2 * i + 1))
            else result -= (1.0 / (2 * i + 1))
            i++
        }
        return String.format("[%d, %.10f]", i, 4 * result)
    }
}