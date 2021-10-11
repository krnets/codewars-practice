#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"
TEST_CASE("testing Consonant value")
{
	SUBCASE("sample tests")
	{
        CHECK(solve("zodiac") == 26);
        CHECK(solve("chruschtschov") == 80);
        CHECK(solve("khrushchev") == 38);
        CHECK(solve("strength") == 57);
        CHECK(solve("catchphrase") == 73);
        CHECK(solve("twelfthstreet") == 103);
        CHECK(solve("mischtschenkoana") == 80);
    }
}
