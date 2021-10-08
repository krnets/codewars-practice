#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing deleteNth")
{
	SUBCASE("Basic_tests")
	{
		CHECK(deleteNth({20, 37, 20, 21}, 1) == std::vector<int>({20, 37, 21}));
		CHECK(deleteNth({1, 1, 3, 3, 7, 2, 2, 2, 2}, 3) == std::vector<int>({1, 1, 3, 3, 7, 2, 2, 2}));
		CHECK(deleteNth({ 1,2,3,1,2,1,2,3 }, 2) == std::vector<int>({ 1,2,3,1,2,3 }));
	}
}
