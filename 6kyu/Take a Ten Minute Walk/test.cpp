#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing IsValidWalk")
{
	using V = std::vector<char>;

	SUBCASE("BasicTests")
	{
		CHECK(isValidWalk(V{'n'}) == false);
		CHECK(isValidWalk(V{'n','s','n','s','n','s','n','s','n','s'}) == true);
		CHECK(isValidWalk(V{'n','s'}) == false);
		CHECK(isValidWalk(V{'n','s','r'}) == false);
		CHECK(isValidWalk(V{'n','s','n','s','n','s','n','s','n','s','n','s'}) == false);
		CHECK(isValidWalk(V{'e','w','e','w','n','s','n','s','e','w'}) == true);
		CHECK(isValidWalk(V{'n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w'}) == false);
		CHECK(isValidWalk(V{'n','s','e','w','n','s','e','w','n','s'}) == true);
		CHECK(isValidWalk(V{'s','e','w','n','n','s','e','w','n','s'}) == true);
		CHECK(isValidWalk(V{'n','s','n','s','n','s','n','s','n','n'}) == false);
		CHECK(isValidWalk(V{'e','e','e','w','n','s','n','s','e','w'}) == false);
	}
}
