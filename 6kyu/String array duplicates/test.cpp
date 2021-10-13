#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing String_array_revisal")
{
	SUBCASE("Example_tests")
	{
		CHECK(dup(vector<string>{"ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"}) == vector<string>{
		      "codewars", "picaniny", "hubububo"});

		CHECK(dup(vector<string>{"abracadabra","allottee","assessee"}) == vector<string>{"abracadabra", "alote",
		      "asese"});

		CHECK(dup(vector<string>{"kelless","keenness"}) == vector<string>{"keles", "kenes"});
	}
}
