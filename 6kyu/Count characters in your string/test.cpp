#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SampleTests")
{
	using m = map<char, unsigned>;

	SUBCASE("should_pass_sample_tests")
	{
		CHECK(countt("aba") == m{{'a', 2}, {'b', 1}});
		CHECK(countt("") == m{});
	}
}
