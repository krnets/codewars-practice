#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing vowelIndices")
{
	SUBCASE("SimpleTests")
	{
		using V = std::vector<int>;

		CHECK(vowelIndices("super") == V{ 2, 4 });
		CHECK(vowelIndices("orAnge") == V{ 1, 3, 6 });
		CHECK(vowelIndices("aZNbUbeOfeRb") == V{ 1, 5, 7, 8, 10 });
		CHECK(vowelIndices(
			      "YZXiNVeUcjOmOSVZVddjVlVOfkchYRTRaccYNYOjURTNNWeYaZPRRYXhQPbkWgTaaacRNhcXgVkgaWWSehOWgmYORVNfaR") == V
		      { 1, 4, 7, 8, 11, 13, 24, 29, 33, 36, 38, 39, 41, 47, 48, 49, 54, 64, 65, 66, 77, 81, 83, 87, 88, 93 });
	}
}
