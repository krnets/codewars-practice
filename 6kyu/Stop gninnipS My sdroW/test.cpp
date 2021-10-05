#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sample_Tests")
{
	SUBCASE("")
	{
		CHECK(spinWords("Welcome") == "emocleW");
		CHECK(spinWords("to") == "to");
		CHECK(spinWords("CodeWars") == "sraWedoC");
	}

	SUBCASE("Mulitple_Words")
	{
		CHECK(spinWords("Hey fellow warriors") == "Hey wollef sroirraw");
		CHECK(spinWords("Burgers are my favorite fruit") == "sregruB are my etirovaf tiurf");
		CHECK(spinWords("Pizza is the best vegetable") == "azziP is the best elbategev");
	}
}
