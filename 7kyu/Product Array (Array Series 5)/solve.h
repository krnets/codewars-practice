#pragma once
/*
#include <numeric>

std::vector<int> productArray(std::vector<int> numbers)
{
	const int product = std::accumulate(numbers.begin(), numbers.end(), 1, std::multiplies());
	std::vector<int> vec;
	vec.reserve(numbers.size());

	for (int num : numbers)
		vec.push_back(product / num);

	return vec;
}
*/

/*
#include <range/v3/numeric/accumulate.hpp>

std::vector<int> productArray(std::vector<int> numbers)
{
	const int product = ranges::accumulate(numbers, 1, std::multiplies());
	std::vector<int> vec;
	vec.reserve(numbers.size());

	for (int num : numbers)
		vec.push_back(product / num);

	return vec;
}
*/

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

std::vector<int> productArray(std::vector<int> numbers)
{
	const int product = ranges::accumulate(numbers, 1, std::multiplies());

	return numbers
		| ranges::views::transform([product](int num) { return product / num; })
		| ranges::to<std::vector<int>>();
}
