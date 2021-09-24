#pragma once

#include <stdint.h>

/*
int digits(uint64_t n)
{
	if (n == 0)
		return 1;

	int count = 0;

	while (n > 0)
	{
		n /= 10;
		count++;
	}
	return count;
}
*/

int digits(uint64_t n)
{
	int count = 0;

	do
	{
		count++;
		n /= 10;
	}
	while (n > 0);

	return count;
}
