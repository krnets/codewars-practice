#pragma once

#include <range/v3/numeric/accumulate.hpp>

/*
int findOdd(const std::vector<int>& numbers)
{
	return ranges::accumulate(numbers, 0, [](int a, int b) { return a ^ b; });
}
*/

int findOdd(const std::vector<int>& numbers)
{
	return ranges::accumulate(numbers, 0, std::bit_xor());
}
