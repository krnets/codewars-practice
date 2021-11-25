#pragma once

#include <bitset>

using std::bitset;

int nextHigher(int value)
{
	int ans = value + 1;;
	auto bits_count = bitset<32>(value).count();

	while (bitset<32>(ans).count() != bits_count)
		++ans;

	return ans;
}
