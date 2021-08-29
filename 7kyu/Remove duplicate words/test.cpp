#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing RemoveDuplicateWords")
{
	SUBCASE("BasicTests")
	{
		CHECK(removeDuplicateWords(
				"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") ==
			"alpha beta gamma delta");

		CHECK(removeDuplicateWords("my cat is cat fat") == "my cat is fat");
	}
}
