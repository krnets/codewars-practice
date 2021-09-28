#pragma once
#include <bitset>

/*
unsigned int reverse_bits(unsigned int n)
{
	if (n == 0) return n;

	auto bits = std::bitset<32>(n);
	std::string s = bits.to_string();
	int i = s.find('1');
	std::reverse(s.begin() + i, s.end());

	return std::stoul(s, 0, 2);
}
*/

unsigned int reverse_bits(unsigned int n)
{
	unsigned ans = 0;

	while (n > 0)
	{
		ans += ans + (n & 1);
		n >>= 1;
	}

	return ans;
}
