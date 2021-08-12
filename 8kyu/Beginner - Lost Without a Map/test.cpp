#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <random>

TEST_CASE("testing the_maps_function")
{
	int random_int();
	std::vector<int> make_random_vector(size_t size);

	SUBCASE("should_return_an_empty_vector_on_an_empty_input")
	{
		const std::vector<int> empty;
		CHECK(maps(empty) == empty);
	}
	SUBCASE("should_return_a_vector_of_the_same_length")
	{
		for (size_t i = 1; i < 145; i += 13)
		{
			const auto input = make_random_vector(i);

			CHECK(maps(input).size() == i);
		}
	}
	SUBCASE("should_return_a_vector_where_the_first_value_is_doubled")
	{
		for (size_t i = 1; i < 145; i += 13)
		{
			const auto input = make_random_vector(i);
			CHECK(maps(input)[0] == input[0] * 2) ;
		}
	}
};

int random_int()
{
	static std::random_device rd;
	static std::mt19937 gen(rd());
	static std::uniform_int_distribution<int> d(-2000, 2000);

	return d(gen);
}

std::vector<int> make_random_vector(size_t size)
{
	std::vector<int> vec(size);
	std::generate(vec.begin(), vec.end(), random_int);

	return vec;
}
