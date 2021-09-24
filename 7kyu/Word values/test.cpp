#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Word_Values")
{
	using namespace std;
	SUBCASE("Example_tests")
	{
		CHECK(wordValue(vector<string>{"abc","abc abc"}) == vector<int>{6, 24});
		CHECK(wordValue(vector<string>{"codewars","abc","xyz"}) == vector<int>{88, 12, 225});
		CHECK(wordValue(vector<string>{"abcdefghijklmnopqrstuvwxyz","stamford bridge","haskellers"}) == vector<int>{351,
		      282, 330});
	}
}
