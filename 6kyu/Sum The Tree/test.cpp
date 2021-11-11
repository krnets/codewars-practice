#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sum The Tree")
{
	SUBCASE("Easy")
	{
		node easyNode = {10, new node{1, nullptr, nullptr}, new node{2, nullptr, nullptr}};
		CHECK(sumTheTreeValues(&easyNode) == 13);
	}
	SUBCASE("Unbalanced")
	{
		node unbalancedNode = {11, new node{0, nullptr, nullptr}, new node{0, nullptr, new node{1, nullptr, nullptr}}};
		CHECK(sumTheTreeValues(&unbalancedNode) == 12);
	}
	SUBCASE("Childless")
	{
		node childlessNode = {5, nullptr, nullptr};
		CHECK(sumTheTreeValues(&childlessNode) == 5);
	}
	SUBCASE("Negative")
	{
		node negNode = {-8, nullptr, nullptr};
		CHECK(sumTheTreeValues(&negNode) == -8);
	}
}
