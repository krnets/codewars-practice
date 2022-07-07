/*
class CircularList<T>(vararg val elements: T) {
    private var pos: Int

    fun next(): T {
        if (pos in 0 until elements.lastIndex) pos++
        else pos = 0

        return elements[pos]
    }

    fun prev(): T {
        if (pos in 1 until elements.size) pos--
        else pos = elements.lastIndex

        return elements[pos]
    }

    init {
        if (elements.isEmpty()) throw Exception("input contains no values")
        this.pos = -1
    }
}
*/

/*
class CircularList<T>(vararg val elements: T) {
    private var pos = -1

    init {
        if (elements.isEmpty()) throw Exception("input contains no values")
    }

    fun next(): T {
        if (pos in 0 until elements.lastIndex) pos++
        else pos = 0

        return elements[pos]
    }

    fun prev(): T {
        if (pos in 1 until elements.size) pos--
        else pos = elements.lastIndex

        return elements[pos]
    }
}
*/

class CircularList<T>(vararg val elements: T) {
    private var pos = -1

    init { if (elements.isEmpty()) throw Exception("input contains no values") }

    fun next(): T = elements.getOrNull(++pos) ?: run { pos = 0; elements[pos] }
    fun prev(): T = elements.getOrNull(--pos) ?: run { pos = elements.lastIndex; elements[pos] }
}
