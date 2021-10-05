#pragma once

#include <bitset>

/*
unsigned int countBits(unsigned long long n)
{
	std::bitset<64> bits(n);

	return bits.count();
}
*/

/*
unsigned int countBits(unsigned long long n)
{
	std::bitset<std::numeric_limits<unsigned long long>::digits> bits(n);

	return bits.count();
}
*/

/*
unsigned int countBits(unsigned long long n)
{
	std::bitset<8 * sizeof n> bits(n);

	return bits.count();
}
*/

unsigned int countBits(unsigned long long n)
{
	std::bitset<CHAR_BIT * sizeof n> bits(n);

	return bits.count();
}

/*
unsigned int countBits(unsigned long long n)
{
	int count = 0;

	while (n > 0)
	{
		count += n & 1;
		n >>= 1;
	}

	return count;
}
*/
