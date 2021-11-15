#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	using vs = std::vector<std::string>;

	SUBCASE("Sample_tests")
	{
		CHECK(uniq(vs{"a","a","b","b","c","a","b","c","c"}) == vs{"a", "b", "c", "a", "b", "c"});
		CHECK(uniq(vs{"a","a","a","b","b","b","c","c","c"}) == vs{"a", "b", "c"});
	}
}
