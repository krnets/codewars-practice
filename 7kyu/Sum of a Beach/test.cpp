#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_tests")
{
	SUBCASE("sample_tests 1")
	{
		CHECK(1 == sum_of_a_beach("SanD"));
		CHECK(1 == sum_of_a_beach("sunshine"));
		CHECK(4 == sum_of_a_beach("sunsunsunsun"));
		CHECK(1 == sum_of_a_beach("123FISH321"));
	}
	SUBCASE("sample_tests 2")
	{
		CHECK(1 == sum_of_a_beach("WAtErSlIde"));
		CHECK(3 == sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN"));
		CHECK(4 == sum_of_a_beach("gOfIshsunesunFiSh"));
		CHECK(0 == sum_of_a_beach("cItYTowNcARShoW"));
	}
}
