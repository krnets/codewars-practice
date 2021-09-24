#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing calculate")
{
	SUBCASE("sample_basic_tests")
	{
		CHECK(calculate("1plus2plus3plus4") == "10");
		CHECK(calculate("1minus2minus3minus4") == "-8");
		CHECK(calculate("1plus2plus3minus4") == "2");
	}
}
