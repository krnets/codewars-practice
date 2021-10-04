#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("Hello_World_Tests")
	{
		CHECK(stringCounter("Hello World", 'o') == 2);
	}
	SUBCASE("Cinical_test_case")
	{
		CHECK(stringCounter("Wait isn't it supposed to be cynical?", 'i') == 4);
	}
	SUBCASE("Lets_see_how_you_handle_this")
	{
		CHECK(stringCounter("I'm gona be the best code warrior ever dad", 'r') == 4);
	}
	SUBCASE("What_do_you_think")
	{
		CHECK(stringCounter("Do you like Harry Potter?", '?') == 1);
	}
}
