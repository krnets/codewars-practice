#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing test_rpg")
{
	SUBCASE("should_pass_some_example_tests")
	{
		CHECK(rps("rock", "scissors") == "Player 1 won!");
		CHECK(rps("rock", "paper") == "Player 2 won!");
		CHECK(rps("rock", "rock") == "Draw!");
	}
}
