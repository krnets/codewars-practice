#pragma once

/*
int maxMultiple(int divisor, int bound)
{
	while (bound % divisor != 0)
	{
		bound--;
	}

	return bound;
}
*/

/*
int maxMultiple(int divisor, int bound)
{
	return divisor * (bound / divisor);
}
*/

int maxMultiple(int divisor, int bound)
{
	return bound - (bound % divisor);
}
