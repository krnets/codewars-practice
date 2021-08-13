#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing planet_id_conversion")
{
	SUBCASE("all planets")
	{
		CHECK(get_planet_name(2) == "Venus");
		CHECK(get_planet_name(5) == "Jupiter");
		CHECK(get_planet_name(3) == "Earth");
		CHECK(get_planet_name(4) == "Mars");
		CHECK(get_planet_name(8) == "Neptune");
		CHECK(get_planet_name(1) == "Mercury");
		CHECK(get_planet_name(7) == "Uranus");
		CHECK(get_planet_name(6) == "Saturn");
	}
}
