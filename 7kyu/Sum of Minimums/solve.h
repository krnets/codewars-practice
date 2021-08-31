#pragma once

#include <numeric>
#include <range/v3/algorithm/min_element.hpp>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/transform.hpp>

/*
int sum_of_minimums(const std::vector<std::vector<int>>& numbers)
{
	int sum = 0;

	for (std::vector<int> v : numbers)
	{
		sum += *std::ranges::min_element(v);
	}

	return sum;
}
*/


int sum_of_minimums(const std::vector<std::vector<int>>& numbers)
{
	auto transform_view = numbers | ranges::views::transform([](auto vec) { return *ranges::min_element(vec); });

	return ranges::accumulate(transform_view, 0);
}

/*
int sum_of_minimums(const std::vector<std::vector<int>>& numbers)
{
	int sum = 0;

	for (std::vector<int> v : numbers)
	{
		sum += *ranges::min_element(v);
	}

	return sum;
}
*/

/*
int sum_of_minimums(const std::vector<std::vector<int>>& numbers)
{
	return std::accumulate(numbers.begin(), numbers.end(), 0, [](int acc, auto v)
	{
		return *ranges::min_element(v) + acc;
	});
}
*/
