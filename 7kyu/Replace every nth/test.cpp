#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("ExampleTest1")
	{
		std::string expected = "Vader soid: No, I am your fother!";

		Kata kata;
		std::string actual = kata.replaceNth("Vader said: No, I am your father!", 2, 'a', 'o');

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest2")
	{
		std::string expected = "Vader said: No, I am your fother!";

		Kata kata;
		std::string actual = kata.replaceNth("Vader said: No, I am your father!", 4, 'a', 'o');

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest3")
	{
		std::string expected = "Vader said: No, I am your father!";

		Kata kata;
		std::string actual = kata.replaceNth("Vader said: No, I am your father!", 6, 'a', 'o');

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest4")
	{
		std::string expected = "Vader said: No, I am your father!";

		Kata kata;
		std::string actual = kata.replaceNth("Vader said: No, I am your father!", 0, 'a', 'o');

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest5")
	{
		std::string expected = "Vader said: No, I am your father!";

		Kata kata;
		std::string actual = kata.replaceNth("Vader said: No, I am your father!", -2, 'a', 'o');

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest6")
	{
		std::string expected = "Vader sayd: No, I am your father!";

		Kata kata;
		std::string actual = kata.replaceNth("Vader said: No, I am your father!", 1, 'i', 'y');

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest7")
	{
		std::string expected = "Luke cries: Noooooioooooioooo!";

		Kata kata;
		std::string actual = kata.replaceNth("Luke cries: Noooooooooooooooo!", 6, 'o', 'i');

		CHECK(actual == expected);
	}
}
