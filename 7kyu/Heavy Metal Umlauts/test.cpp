#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Hëävÿ Mëtäl Ümläüts")
{
	SUBCASE("BasicTest1")
	{
		std::string expected = "Ännöüncïng thë Mäcböök Äïr Güïtär";

		std::string actual = heavyMetalUmlauts("Announcing the Macbook Air Guitar");

		CHECK(actual == expected);
	}
	SUBCASE("BasicTest2")
	{
		std::string expected = "Fäcëböök ïntrödücës nëw hëävÿ mëtäl rëäctïön büttöns";

		std::string actual = heavyMetalUmlauts("Facebook introduces new heavy metal reaction buttons");

		CHECK_EQ(actual, expected);
	}
	SUBCASE("BasicTest3")
	{
		std::string expected = "Ströng sälës öf Gööglë's VR Mëtälhëädsëts sënd tëch stöck prïcës söärïng";

		std::string actual = heavyMetalUmlauts(
			"Strong sales of Google's VR Metalheadsets send tech stock prices soaring");

		CHECK_EQ(actual, expected);
	}
	SUBCASE("BasicTest4")
	{
		std::string expected = "Vëgän Bläck Mëtäl Chëf hïts thë bïg tïmë ön Ämäzön TV";

		std::string actual = heavyMetalUmlauts("Vegan Black Metal Chef hits the big time on Amazon TV");

		CHECK_EQ(actual, expected);
	}
}
