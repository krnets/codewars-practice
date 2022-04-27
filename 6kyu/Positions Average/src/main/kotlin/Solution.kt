package solution

/*
object PositionAverage {
    fun posAverage(s: String): Double {
        val list = s.split(", ")
        var total = list.size * (list.size - 1) / 2
        var common = 0

        for (i in 0 until list.lastIndex)
            for (j in i + 1..list.lastIndex)
                common += list[i].zip(list[j]).count { it.first == it.second }

        return common.toDouble() / list.first().length / total * 100
    }
}*/

/*
object PositionAverage {
    fun posAverage(s: String): Double {
        val list = s.split(", ")
        val combinations = list.first().length * list.size * (list.size - 1) / 2

        val common = list.mapIndexed { index, a ->
            list.drop(index + 1).sumOf { b ->
                a.zip(b).count { it.first == it.second }
            }
        }
        return common.sum().toDouble() / combinations * 100
    }
}
*/

/*
object PositionAverage {
    fun posAverage(s: String): Double = s.split(", ").let { list ->
        list.mapIndexed { index, a ->
            list.drop(index + 1).sumOf { b ->
                a.zip(b).count { it.first == it.second }
            }
        }.sum().toDouble() / (list.first().length * list.size * (list.size - 1) / 2) * 100
    }
}
*/

object PositionAverage {
    fun posAverage(s: String): Double = s.split(", ").let { list ->
        list.mapIndexed { index, a ->
            list.drop(index + 1).sumOf { b ->
                a.zip(b).count { it.first == it.second }
            }
        }.sum() * 100.0 / (list.first().length * list.size * (list.size - 1) / 2)
    }
}