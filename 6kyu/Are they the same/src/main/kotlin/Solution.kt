fun comp(a: IntArray?, b: IntArray?): Boolean {
    return (b != null) and (a!!.sorted().map { it * it } == b!!.sorted())
}