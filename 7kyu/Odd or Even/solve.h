#pragma once

#include <numeric>

std::string odd_or_even(const std::vector<int>& arr)
{
	int sum = std::accumulate(arr.begin(), arr.end(), 0);

	return sum % 2 == 0 ? "even" : "odd";
}
