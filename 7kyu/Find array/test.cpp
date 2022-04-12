#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"
#define SVEC vector<std::string>
#define IVEC vector<int>

TEST_CASE("testing Find array")
{
	SUBCASE("sample test")
	{
		CHECK(find_array(SVEC(5, "a"), {2, 4}) == SVEC(2, "a"));
		CHECK(find_array(IVEC{0, 1, 5, 2, 1, 8, 9, 1, 5}, {1, 4, 7}) == IVEC(3, 1));
	}
}
