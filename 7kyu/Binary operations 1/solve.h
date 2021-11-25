#pragma once
#include <bitset>

/*
int flip_bit(int value, size_t index)
{
	std::bitset<32> bits(value);

	bits.flip(index - 1);

	return bits.to_ulong();
}
*/

int flip_bit(int value, size_t index)
{
	int bit_mask = (1 << (index - 1));

	return value ^ bit_mask;
}
