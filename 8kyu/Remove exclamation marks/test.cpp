#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing RemoveExclamationMarks")
{
	SUBCASE("BasicTests")
	{
		CHECK(removeExclamationMarks("Hello World!") == "Hello World");
		CHECK(removeExclamationMarks("Hello World!!!") == "Hello World");
		CHECK(removeExclamationMarks("Hi! Hello!") == "Hi Hello");
		CHECK(removeExclamationMarks("Hi!!! Hello!") == "Hi Hello");
		CHECK(removeExclamationMarks("Hi! He!l!lo!") == "Hi Hello");
	}
}
