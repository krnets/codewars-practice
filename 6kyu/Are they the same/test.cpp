#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Comp_Tests")
{
	using std::vector;

	SUBCASE("Tests_1")
	{
		vector<int> a = {121, 144, 19, 161, 19, 144, 19, 11};
		vector<int> b = {14641, 20736, 361, 25921, 361, 20736, 361, 121};
		CHECK(Same::comp(a,b) == true);
	}

	SUBCASE("Tests_2")
	{
		vector<int> a = {121, 144, 19, 161, 19, 144, 19, 11};
		vector<int> b = {14641, 20736, 361, 25921, 361, 20736, 362, 121};
		CHECK(Same::comp(a,b) == false);
	}

	SUBCASE("Tests_3")
	{
		vector<int> a = {};
		vector<int> b = {361, 121};
		CHECK(Same::comp(a,b) == false);
	}
}
