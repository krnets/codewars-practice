#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing reverse_words")
{
	SUBCASE("Sample_Test_Cases")
	{
		CHECK(reverse_words("apple") == "elppa");
		CHECK(reverse_words("This is an example!") == "sihT si na !elpmaxe");
		CHECK(reverse_words("double  spaces") == "elbuod  secaps");
		CHECK(reverse_words("The quick brown fox jumps over the lazy dog.") == "ehT kciuq nworb xof spmuj revo eht yzal .god");
		CHECK(reverse_words("a b c d") == "a b c d");
		CHECK(reverse_words("double  spaced  words") == "elbuod  decaps  sdrow");
		CHECK(reverse_words("") == "");
		CHECK(reverse_words("ab   ba   cd") == "ba   ab   dc");
	}
}
