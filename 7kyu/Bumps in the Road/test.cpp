#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing bumps_tests")
{
	SUBCASE("basic_tests")
	{
		CHECK(bumps("n") == "Woohoo!");
		CHECK(bumps("_nnnnnnn_n__n______nn__nn_nnn") == "Car Dead");
		CHECK(bumps("______n___n_") == "Woohoo!");
		CHECK(bumps("nnnnnnnnnnnnnnnnnnnnn") == "Car Dead");
	}
}
