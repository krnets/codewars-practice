#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Counting Valleys")
{
    SUBCASE("should_handle_simple_situations")
    {
        CHECK(countValleys("DU") == 1);
        CHECK(countValleys("FFFFFFFF") == 0);
    }
    
    SUBCASE("should_handle_basics")
    {
      CHECK(countValleys("UFFDDFDUDFUFU") == 1);
      CHECK(countValleys("UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU") == 3);
      CHECK(countValleys("UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU") == 6);
      CHECK(countValleys("UFFDDFDUDFUFUUFFDDFDUDFUFU") == 2);
      CHECK(countValleys("UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU") == 4);
      CHECK(countValleys("DFFFU") == 1);
      CHECK(countValleys("UFFFD") == 0);
      CHECK(countValleys("DFFFD") == 0);
      CHECK(countValleys("UFFFU") == 0); 
    }
}
