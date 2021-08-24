#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing isTriangle")
{
	SUBCASE("Zero_ReturnsFalse")
	{
		CHECK(Triangle::isTriangle(0,0,0) == false);
		CHECK(Triangle::isTriangle(0,1,2) == false);
	}

	SUBCASE("Negative_ReturnsFalse")
	{
		CHECK(Triangle::isTriangle(-17,15,20) == false);
		CHECK(Triangle::isTriangle(-17,-15,20) == false);
	}

	SUBCASE("ValidTriangles_ReturnsTrue")
	{
		CHECK(Triangle::isTriangle(15,17,20) == true);
		CHECK(Triangle::isTriangle(10,10,10) == true);
		CHECK(Triangle::isTriangle(10,5,10) == true);
	}

	SUBCASE("InvalidTriangles_ReturnsFalse")
	{
		CHECK(Triangle::isTriangle(3,2,1) == false);
		CHECK(Triangle::isTriangle(10,10,20) == false);
	}
	SUBCASE("Limits_ReturnsTrue")
	{
		CHECK(Triangle::isTriangle( 2147483647,2147483647,2147483647 ) == true);
	}
	SUBCASE("Random_ReturnsFalse")
	{
		CHECK(Triangle::isTriangle( -128236739,43899390,1720549145 ) == false);
		CHECK(Triangle::isTriangle( 138887893,826445426,1485363197 ) == false);
	}
	SUBCASE("Random_ReturnsTrue")
	{
		CHECK(Triangle::isTriangle( 1422495321,661644344,1528621437 ) == true);
		CHECK(Triangle::isTriangle( 1206116186,802823470,1023398570 ) == true);
		CHECK(Triangle::isTriangle( 1799833952,699511349,1649828627 ) == true);
	}
}
