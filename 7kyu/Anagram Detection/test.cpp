#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing IsAnagram")
{
	SUBCASE("BasicTests")
	{
		CHECK(isAnagram("foefet", "toffee") == true);
		CHECK(isAnagram("Buckethead", "DeathCubeK") == true);
		CHECK(isAnagram("Twoo", "WooT") == true);
		CHECK(isAnagram("dumble", "bumble") == false);
		CHECK(isAnagram("around", "round") == false);
		CHECK(isAnagram("ound", "round") == false);
		CHECK(isAnagram("apple", "pale") == false);
		CHECK(isAnagram("apple", "appeal") == false);
		CHECK(isAnagram("apple", "appeal") == false);
		CHECK(isAnagram("", "") == true);
	}
}
