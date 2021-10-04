#pragma once
#include <vector>
#include <algorithm>
#include <functional>

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using std::vector;

/*
std::vector<int> invert(std::vector<int> values)
{
	for (int& value : values) value = -value;

	return values;
}
*/

/*
std::vector<int> invert(std::vector<int> values)
{
	std::transform(values.begin(), values.end(), values.begin(), [](const int& a) { return -a; });

	return values;
}
*/

/*
std::vector<int> invert(std::vector<int> values)
{
	std::transform(values.begin(), values.end(), values.begin(), std::negate());

	return values;
}
*/

vector<int> invert(vector<int> values)
{
	return values
		| ranges::views::transform(std::negate())
		| ranges::to<vector<int>>();
}
