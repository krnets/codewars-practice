package solution

import org.junit.Test
import kotlin.test.assertEquals

class OpstringsTest {
    private fun testing(actual: String, expected: String) {
        assertEquals(expected, actual)
    }

    @Test
    fun `rotate test`() {
        println("Fixed Tests rot")
        testing(
            Opstrings.oper(Opstrings::rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"),
            "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif"
        )
        testing(
            Opstrings.oper(Opstrings::rot, "rkKv\ncofM\nzXkh\nflCB"),
            "BClf\nhkXz\nMfoc\nvKkr"
        )
    }

    @Test
    fun `selfieAndRot test`() {
        println("Fixed Tests selfieAndRot")
        testing(
            Opstrings.oper(Opstrings::selfieAndRot, "abcd\nefgh\nijkl\nmnop"),
            "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
        )
        testing(
            Opstrings.oper(Opstrings::selfieAndRot, "xZBV\njsbS\nJcpN\nfVnP"),
            "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx"
        )
        testing(
            Opstrings.oper(Opstrings::selfieAndRot, "uLcq\nJkuL\nYirX\nnwMB"),
            "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu"
        )
    }
}