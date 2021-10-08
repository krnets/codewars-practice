#pragma once

#include <unordered_map>

std::pair<std::size_t, std::size_t> two_sum(const std::vector<int>& numbers, int target)
{
	std::unordered_map<int, size_t> map;

	for (size_t i = 0; i < numbers.size(); ++i)
	{
		int complement = target - numbers[i];

		if (map.find(complement) != map.end())
			return std::make_pair(map[complement], i);

		map[numbers[i]] = i;
	}

	return std::make_pair(-1, -1);
}
