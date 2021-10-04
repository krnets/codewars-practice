#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ReverseSeq")
{
	using v = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(reverseSeq(1) == v{1});
		CHECK(reverseSeq(2) == v{2, 1});
		CHECK(reverseSeq(5) == v{5, 4, 3, 2, 1});
		CHECK(reverseSeq(10) == v{10, 9, 8, 7, 6, 5, 4, 3, 2, 1});
	}
}
