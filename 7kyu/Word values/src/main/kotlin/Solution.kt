object Solution {
    fun nameValue(arr: Array<String>): IntArray {
        return arr.mapIndexed { index, word ->
            word.sumOf {
                if (it.isLetter()) it - 'a' + 1
                else 0
            } * (index + 1)
        }.toIntArray()
    }
}