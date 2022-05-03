import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun basic() {
        assertEquals(
            "Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC\n" +
                    "Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC\n" +
                    "Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C\n\n" +
                    "Reverse Frame 1: GCT AAT ATA AGG CTT GCG GTG TCA CCT\n" +
                    "Reverse Frame 2: G CTA ATA TAA GGC TTG CGG TGT CAC CT\n" +
                    "Reverse Frame 3: GC TAA TAT AAG GCT TGC GGT GTC ACC T",
            DNADecomposer.decomposeDoubleStrand("AGGTGACACCGCAAGCCTTATATTAGC")
        )
    }
}