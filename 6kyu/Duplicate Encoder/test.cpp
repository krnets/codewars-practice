#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing duplicate_encoder")
{
	SUBCASE("Basic_Tests")
	{
		CHECK(duplicate_encoder("din") == "(((");
		CHECK(duplicate_encoder("recede") == "()()()");
		CHECK(duplicate_encoder("Success") == ")())())");
		CHECK(duplicate_encoder("CodeWarrior") == "()(((())())");
		CHECK(duplicate_encoder("Supralapsarian") == ")()))()))))()(");
		CHECK(duplicate_encoder("(( @") == "))((");
		CHECK(duplicate_encoder(" ( ( )") == ")))))(");
	}
}
