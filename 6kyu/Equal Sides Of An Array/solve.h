#pragma once

#include <range/v3/numeric/accumulate.hpp>

int find_even_index(const std::vector<int> numbers)
{
	int left = 0;
	int right = ranges::accumulate(numbers, 0);

	for (int i = 0; i < numbers.size(); ++i)
	{
		right -= numbers[i];

		if (left == right)
			return i;

		left += numbers[i];
	}

	return -1;
}
