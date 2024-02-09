/*
object FileNameExtractor {
    fun extractFileName(dirtyFileName: String): String {
        return dirtyFileName.replace(Regex("(\\d+)_(.*)\\.(.*)"), "$2")
    }
}
*/

object FileNameExtractor {
    fun extractFileName(dirtyFileName: String): String {
        return dirtyFileName.replace(Regex("""(\d+)_(.*)\.(.*)"""), "$2")
    }
}

/*
object FileNameExtractor {
    fun extractFileName(dirtyFileName: String): String {
        return dirtyFileName.substringAfter('_').substringBeforeLast('.')
    }
}
*/
