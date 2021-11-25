#pragma once

#include <bitset>

/*
std::vector<int> showBits(int n)
{
	std::string s = std::bitset<32>(n).to_string();
	std::vector<int> v(32);

	for (int i = 0; i < 32; ++i)
	{
		v[i] = s[i] - '0';
	}

	return v;
}
*/

std::vector<int> showBits(int n)
{
	std::bitset<32> bits(n);
	std::vector<int> v(32);

	for (int i = 0; i < 32; ++i)
	{
		v[i] = bits.test(31 - i);
	}

	return v;
}


/*
std::vector<int> showBits(int n)
{
	std::vector<int> v(32);

	for (int i = v.size() - 1; i >= 0; --i)
	{
		v[i] = n & 1;
		n >>= 1;
	}

	return v;
}
*/
