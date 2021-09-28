#pragma once

#include <vector>

/*
std::vector<int> remove_values(std::vector<int> integers, std::vector<int> values)
{
	std::vector<int> v;
	std::set s(values.begin(), values.end());

	for (int x : integers)
		if (s.find(x) == s.end())
			v.push_back(x);

	return v;
}
*/


std::vector<int> remove_values(std::vector<int> integers, std::vector<int> values)
{
	std::vector<int> v;
	std::set s(values.begin(), values.end());

	for (int x : integers)
		if (!s.count(x))
			v.push_back(x);

	return v;
}
