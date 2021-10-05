#pragma once

#include <range/v3/algorithm/count_if.hpp>

size_t duplicateCount(const char* in)
{
	std::array<int, 128> freq = {0};

	while (*in != '\0') freq[tolower(*in++)]++;

	auto pred = [](int x) { return x > 1; };

	return ranges::count_if(freq, pred);
}
