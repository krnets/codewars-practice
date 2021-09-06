#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing AlphabeticalAddition")
{
	SUBCASE("FixedTests")
	{
		using vec = std::vector<char>;

		CHECK(add_letters(vec{'a', 'b', 'c'}) == 'f');
		CHECK(add_letters(vec{'z'}) == 'z');
		CHECK(add_letters(vec{'a', 'b'}) == 'c');
		CHECK(add_letters(vec{'c'}) == 'c');
		CHECK(add_letters(vec{'z', 'a'}) == 'a');
		CHECK(add_letters(vec{'y', 'c', 'b'}) == 'd');
		CHECK(add_letters(vec{}) == 'z');
	}
}
