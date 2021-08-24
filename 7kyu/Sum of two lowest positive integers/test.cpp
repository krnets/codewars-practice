#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <random>
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing sumTwoSmallestNumbers")
{
	SUBCASE("BasicTest")
		CHECK(sumTwoSmallestNumbers({ 5, 8, 12, 19, 22 }) == 13);

	SUBCASE("ExtendedTest1")
		CHECK(sumTwoSmallestNumbers({15, 28, 4, 2, 43}) == 6);

	SUBCASE("ExtendedTest2")
		CHECK(sumTwoSmallestNumbers({3, 87, 45, 12, 7}) == 10);

	SUBCASE("ExtendedTest3")
		CHECK(sumTwoSmallestNumbers({2000000000, 2000000000, 2000000000, 2000000000, 2000000000}) == 4000000000);

	SUBCASE("ExtendedTest4")
		CHECK(sumTwoSmallestNumbers({1000, 2, 3}) == 5);


	SUBCASE("RandomTests")
	{
		auto solution = [](std::vector<int> numbers)
		{
			std::sort(numbers.begin(), numbers.end());

			return static_cast<long>(numbers[0]) + static_cast<long>(numbers[1]);
		};

		std::default_random_engine generator{std::random_device()()};
		std::uniform_int_distribution<int> distributor(1, INT_MAX);
		std::uniform_int_distribution<std::vector<int>::size_type> sizeDistribution(4, 20);

		for (int i = 0; i < 100; i++)
		{
			int length = sizeDistribution(generator);

			std::printf("Test for:\n");
			std::vector<int> numbers;
			for (int j = 0; j < length; j++)
			{
				int n = distributor(generator);
				numbers.push_back(n);

				std::printf("%d", n);

				if (j != length - 1)
				{
					std::printf(", ");
				}
			}
			std::printf("\n<hr>\n");

			long expected = solution(numbers);
			long actual = sumTwoSmallestNumbers(numbers);

			CHECK(actual == expected);
		}
	}
}
