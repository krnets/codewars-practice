#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing stringify_function")
{
	SUBCASE("should_pass_the_example_tests_as_shown_in_the_description")
	{
		CHECK(stringify(new Node(1, new Node(2, new Node(3)))) == "1 -> 2 -> 3 -> nullptr");
		CHECK(stringify(new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))) ==
			"0 -> 1 -> 4 -> 9 -> 16 -> nullptr");
		CHECK(stringify(nullptr) == "nullptr");
	}
}
