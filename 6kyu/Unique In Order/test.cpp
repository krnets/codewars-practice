#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing UniqueInOrder")
{
	using VI = std::vector<int>;
	using VC = std::vector<char>;

	SUBCASE("BasicTests")
	{
		CHECK(uniqueInOrder("") == VC{});
		CHECK(uniqueInOrder("AA") == VC{'A'});
		CHECK(uniqueInOrder("A") == VC{'A'});
		CHECK(uniqueInOrder("AAAABBBCCDAABBB") == VC{'A', 'B', 'C', 'D', 'A', 'B'});
		CHECK(uniqueInOrder("AADD") == VC{'A', 'D'});
		CHECK(uniqueInOrder("AAD") == VC{'A', 'D'});
		CHECK(uniqueInOrder("ADD") == VC{'A', 'D'});
		CHECK(uniqueInOrder("ABBCcAD") == VC{'A', 'B', 'C', 'c', 'A', 'D'});
		CHECK(uniqueInOrder(VI{1, 2, 3, 3}) == VI{1, 2, 3});
		CHECK(uniqueInOrder(VC{'a', 'b', 'b'}) == VC{'a', 'b'});
	}
}
