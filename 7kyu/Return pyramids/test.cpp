#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Pyramid")
{
	SUBCASE("BasicTests")
	{
		CHECK(pyramid(1) == "/\\\n");
		CHECK(pyramid(2) == " /\\\n/__\\\n");
		CHECK(pyramid(4) == "   /\\\n  /  \\\n /    \\\n/______\\\n");

		CHECK(pyramid(6) == "     /\\\n    /  \\\n   /    \\\n  /      \\\n /        \\\n/__________\\\n");
		//     /\\\n
		//    /  \\\n
		//   /    \\\n
		//  /      \\\n
		// /        \\\n
		///__________\\\n

		CHECK(pyramid(10) ==
			"         /\\\n        /  \\\n       /    \\\n      /      \\\n     /        \\\n    /          \\\n   /            \\\n  /              \\\n /                \\\n/__________________\\\n")
		;
	}
}
