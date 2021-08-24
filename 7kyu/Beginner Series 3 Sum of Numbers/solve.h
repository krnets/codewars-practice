#pragma once

/*
int get_sum(int a, int b)
{
	if (a == b) return a;

	int sum = 0;

	for (int i = std::min(a, b); i <= std::max(a, b); ++i)
	{
		sum += i;
	}

	return sum;
}
*/


int get_sum(int a, int b)
{
	return (a + b) * (std::abs(a - b) + 1) / 2;
}
