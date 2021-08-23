#pragma once


/*
unsigned int hotpo(unsigned int n)
{
	int count = 0;

	while (n > 1)
	{
		if (n % 2 == 0)
			n /= 2;
		else n = 3 * n + 1;

		count++;
	}

	return count;
}
*/


unsigned int hotpo(unsigned int n)
{
	if (n == 1) return 0;

	if (n % 2 == 0)
		return 1 + hotpo(n /= 2);

	return 1 + hotpo(3 * n + 1);
}
