import org.junit.Assert.assertEquals
import org.junit.Test

class FileNameExtractorTest {
    @Test
    fun testSample() {
        assertEquals(
            "FILE_NAME.EXTENSION",
            FileNameExtractor.extractFileName("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION")
        )
        assertEquals(
            "FILE_NAME.EXTENSION",
            FileNameExtractor.extractFileName("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34")
        )
        assertEquals(
            "This_is_an_otherExample.mpg",
            FileNameExtractor.extractFileName("1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34")
        )
        assertEquals(
            "myFile.tar",
            FileNameExtractor.extractFileName("1231231223123131_myFile.tar.gz2")
        )
    }
}
