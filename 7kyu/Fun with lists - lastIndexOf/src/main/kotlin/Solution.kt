package kata

object Kata {
    fun lastIndexOf(head: Node?, value: Any): Int {
        var valueIdx = -1
        var index = 0
        var currNode = head

        while (currNode != null) {
            if (currNode.data == value)
                valueIdx = index

            currNode = currNode.next
            index++
        }
        return valueIdx
    }
}

data class Node(val data: Any?, val next: Node? = null)
