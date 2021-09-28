#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fly_tests")
{
	SUBCASE("Basic_tests")
	{
		CHECK(flyBy("xxxxxx", "====T") == "ooooox");
		CHECK(flyBy("xxxxxxxxx", "==T") == "oooxxxxxx");
		CHECK(flyBy("xxxxxxxxxxxxxxx", "=========T") == "ooooooooooxxxxx");
	}
}
