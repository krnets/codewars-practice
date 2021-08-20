#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <random>
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Guesser")
{
	SUBCASE("should_return_true_for_correct_guesses")
	{
		Guesser guesser(10, 2);
		CHECK(guesser.guess(10) == true);
	};
	SUBCASE("should_allow_multiple_correct_guesses")
	{
		Guesser guesser(10, 2);
		for (int i = 0; i < 10; ++i)
			CHECK(guesser.guess(10) == true);
	};
	SUBCASE("should_return_false_for_incorrect_guesses")
	{
		Guesser guesser(10, 2);
		CHECK(guesser.guess(1) == false);
	};
	SUBCASE("should_throw_if_lives_ran_out")
	{
		Guesser guesser(10, 2);
		guesser.guess(1);
		guesser.guess(2);
		CHECK_THROWS_AS(guesser.guess (10), std::exception);
	};

	SUBCASE("should_pass_some_random_tests")
	{
		std::mt19937 engine{std::random_device{}()};
		std::uniform_int_distribution<> random_number{0, 9};
		std::uniform_int_distribution<> random_lives{0, 10};
		for (int i = 0; i < 10; ++i)
		{
			const int number = random_number(engine);
			const int lives = random_lives(engine);
			int current_lives = lives;
			Guesser guesser(number, lives);
			for (int j = 0; j < 20; ++j)
			{
				int guess = random_number(engine);
				if (current_lives > 0)
				{
					CHECK(guesser.guess(guess) == (guess == number));

					if (guess != number)
						--current_lives;
				}
				else
				{
					CHECK_THROWS_AS(guesser.guess(guess), std::exception);
				}
			}
		}
	};
};
