#pragma once

unsigned halving_sum(unsigned n)
{
	unsigned sum = 0;

	while (n > 0)
	{
		sum += n;
		n /= 2;
	}

	return sum;
}
