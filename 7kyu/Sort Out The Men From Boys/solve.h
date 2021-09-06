#pragma once

#include <set>

/*
std::vector<int> menFromBoys(std::vector<int> values)
{
	std::set<int> set;
	std::vector<int> ans;

	for (int value : values) set.insert(value);

	for (int value : set)
		if (value % 2 == 0)
			ans.push_back(value);

	std::for_each(set.rbegin(), set.rend(), [&ans](int x)
	{
		if (x % 2 != 0)
			ans.push_back(x);
	});

	return ans;
}
*/

/*
std::vector<int> menFromBoys(std::vector<int> values)
{
	if (std::ranges::none_of(values, [](int x) { return x % 2 == 0; }))
		return values;

	std::set unique(values.begin(), values.end());
	std::vector<int> ans;

	for (int value : unique)
		if (value % 2 == 0)
			ans.push_back(value);

	std::for_each(unique.rbegin(), unique.rend(), [&ans](int x)
	{
		if (x % 2 != 0)
			ans.push_back(x);
	});

	return ans;
}
*/

std::vector<int> menFromBoys(std::vector<int> values)
{
	auto even = [](int x) { return x % 2 == 0; };

	if (std::ranges::none_of(values, even))
		return values;

	auto mid = std::partition(values.begin(), values.end(), even);
	std::sort(values.begin(), mid);
	std::sort(mid, values.end(), std::greater());

	auto end = std::unique(values.begin(), values.end());
	values.erase(end, values.end());

	return values;
}
