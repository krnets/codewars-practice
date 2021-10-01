#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sample_tests")
{
	using vecs = std::vector<std::string>;

	SUBCASE("Simple_case")
	{
		vecs expected{"quick", "brown", "jumps"};
		CHECK(filter_long_words("The quick brown fox jumps over the lazy dog", 4) == expected);
	}
	SUBCASE("All_false")
	{
		vecs expected{};
		CHECK(filter_long_words("The quick brown fox jumps over the lazy dog", 5) == expected);
	}
	SUBCASE("All_true")
	{
		vecs expected{"The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"};
		CHECK(filter_long_words("The quick brown fox jumps over the lazy dog", 1) == expected);
	}
}
