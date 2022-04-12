/*
object EnoughIsEnough {
    fun deleteNth(elements: IntArray, maxOcurrences: Int): IntArray {
        val list = mutableListOf<Int>()
        val freqMap = mutableMapOf<Int, Int>()

        elements.forEach {
            var count = freqMap[it] ?: 0

            if (count < maxOcurrences) {
                list.add(it)
                ++count
                freqMap[it] = count
            }
        }
        return list.toIntArray()
    }
}*/

/*
object EnoughIsEnough {
    fun deleteNth(elements: IntArray, maxOcurrences: Int): IntArray {
        val freqMap = mutableMapOf<Int, Int>()

        return elements.asSequence()
            .onEach { freqMap[it] = 1 + freqMap.getOrDefault(it, 0) }
            .filter { freqMap[it]!! <= maxOcurrences }
            .toList().toIntArray()
    }
}
*/

object EnoughIsEnough {
    fun deleteNth(elements: IntArray, maxOcurrences: Int): IntArray {
        val freqMap = mutableMapOf<Int, Int>()

        return elements
            .filter { freqMap.merge(it, 1, Int::plus)!! <= maxOcurrences }
            .toIntArray()
    }
}
