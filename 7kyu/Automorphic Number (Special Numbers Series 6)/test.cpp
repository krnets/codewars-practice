#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing AutoMorphic")
{
	SUBCASE("One_Digit_Number")
	{
		CHECK(autoMorphic(1) == "Automorphic");
		CHECK(autoMorphic(3) == "Not!!");
		CHECK(autoMorphic(6) == "Automorphic");
		CHECK(autoMorphic(9) == "Not!!");
	}

	SUBCASE("To_Digit_Number")
	{
		CHECK(autoMorphic(25) == "Automorphic");
		CHECK(autoMorphic(13) == "Not!!");
		CHECK(autoMorphic(76) == "Automorphic");
		CHECK(autoMorphic(95) == "Not!!");
	}

	SUBCASE("Larger_Number")
	{
		CHECK(autoMorphic(625) == "Automorphic");
		CHECK(autoMorphic(225) == "Not!!");
		CHECK(autoMorphic(425) == "Not!!");
		CHECK(autoMorphic(399) == "Not!!");
	}
}
