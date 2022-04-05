#pragma once

#include <cmath>

/*
unsigned int sum_cubes(unsigned int n)
{
	unsigned sum = 0;

	for (int i = 1; i <= n; ++i)
	{
		sum += pow(i, 3);
	}

	return sum;
}
*/

/*
unsigned int sum_cubes(unsigned int n)
{
	return pow(n * (n + 1) / 2, 2);
}
*/

unsigned int sum_cubes(unsigned int n)
{
	return n == 1 ? 1 : n * n * n + sum_cubes(n - 1);
}
