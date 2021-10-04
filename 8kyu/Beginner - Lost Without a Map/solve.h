#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using std::vector;

/*
vector<int> maps(const vector<int>& values)
{
	vector<int> result;
	result.reserve(values.size());

	for (const int value : values)
		result.push_back(2 * value);

	return result;
}
*/

/*
vector<int> maps(const vector<int>& values)
{
	vector<int> result = values;

	for (int i = 0; i < result.size(); ++i)
	{
		result[i] *= 2;
	}

	return result;
}
*/

/*
vector<int> maps(const vector<int>& values)
{
	vector<int> result = values;

	for (int& x : result) x *= 2;

	return result;
}
*/

vector<int> maps(const vector<int>& values)
{
	return values
		| ranges::views::transform([](int x) { return x * 2; })
		| ranges::to<vector<int>>();
}
