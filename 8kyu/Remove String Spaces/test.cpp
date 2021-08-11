#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing remove string spaces")
{
	SUBCASE("basic test")
	{
		CHECK(no_space("8 j 8   mBliB8g  imjB8B8  jl  B") == "8j8mBliB8gimjB8B8jlB");
		CHECK(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd") == "88Bifk8hB8BB8BBBB888chl8BhBfd");
		CHECK(no_space("8aaaaa dddd r     ") == "8aaaaaddddr");
		CHECK(no_space("jfBm  gk lf8hg  88lbe8 ") == "jfBmgklf8hg88lbe8");
		CHECK(no_space("8j aam") == "8jaam");
	}
}
