#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Vaporcode")
{
	SUBCASE("BasicTests")
	{
		CHECK(vaporcode("Let's go to the movies") == "L  E  T  '  S  G  O  T  O  T  H  E  M  O  V  I  E  S");
		CHECK(vaporcode("Why isn't my code working?") ==
			"W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?");
	}
}
