package wallpaper

import org.junit.Test
import org.junit.Assert.*

class EasyWallpaperTest {
    @Test
    fun basicTests() {
        assertEquals("zero", wallpaper(0.0, 3.5, 3.0))
        assertEquals("ten", wallpaper(4.0, 3.5, 3.0))
        assertEquals("sixteen", wallpaper(6.1, 6.7, 2.81))
        assertEquals("sixteen", wallpaper(6.3, 4.5, 3.29))
        assertEquals("sixteen", wallpaper(7.8, 2.9, 3.29))
        assertEquals("seventeen", wallpaper(6.3, 5.8, 3.13))
    }
}