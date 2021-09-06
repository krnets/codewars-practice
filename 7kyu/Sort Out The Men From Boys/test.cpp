#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sort_Out_The_Men_From_Boys")
{
	using vec = std::vector<int>;

	SUBCASE("Check_Positive_Values")
	{
		CHECK(menFromBoys(vec{7, 3, 14, 17}) == vec{14, 17, 7, 3});
		CHECK(menFromBoys(vec{2, 43, 95, 90, 37}) == vec{2, 90, 95, 43, 37});
		CHECK(menFromBoys(vec{20, 33, 50, 34, 43, 46}) == vec{20, 34, 46, 50, 43, 33});
		CHECK(menFromBoys(vec{82, 91, 72, 76, 76, 100, 85}) == vec{72, 76, 82, 100, 91, 85});
		CHECK(menFromBoys(vec{2, 15, 17, 15, 2, 10, 10, 17, 1, 1}) == vec{2, 10, 17, 15, 1});
	}
	SUBCASE("Check_Negative_Values")
	{
		CHECK(menFromBoys(vec{-32, -39, -35, -41}) == vec{-32, -35, -39, -41});
		CHECK(menFromBoys(vec{-64, -71, -63, -66, -65}) == vec{-66, -64, -63, -65, -71});
		CHECK(menFromBoys(vec{-94, -99, -100, -99, -96, -99}) == vec{-100, -96, -94, -99});
		CHECK(menFromBoys(vec{-53, -26, -53, -27, -49, -51, -14}) == vec{-26, -14, -27, -49, -51, -53});
		CHECK(menFromBoys(vec{-17, -45, -15, -33, -85, -56, -86, -30}) == vec{-86, -56, -30, -15, -17, -33, -45, -85});
	}
	SUBCASE("Check_Mixed_Values")
	{
		CHECK(menFromBoys(vec{12, 89, -38, -78}) == vec{-78, -38, 12, 89});
		CHECK(menFromBoys(vec{2, -43, 95, -90, 37}) == vec{-90, 2, 95, 37, -43});
		CHECK(menFromBoys(vec{82, -61, -87, -12, 21, 1}) == vec{-12, 82, 21, 1, -61, -87});
		CHECK(menFromBoys(vec{63, -57, 76, -85, 88, 2, -28}) == vec{-28, 2, 76, 88, 63, -57, -85});
		CHECK(menFromBoys(vec{49, 818, -282, 900, 928, 281, -282, -1}) == vec{-282, 818, 900, 928, 281, 49, -1});
	}
	SUBCASE("Check_Random_Values")
	{
		CHECK(menFromBoys(vec{-33, 99, -9, -47}) == vec{-33, 99, -9, -47 });
	}
}
