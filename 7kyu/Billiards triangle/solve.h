#pragma once

/*
int pyramid(int n)
{
	return (sqrt(8 * n + 1) - 1) / 2;
}
*/

/*
int pyramid(int n)
{
	int levels = 0, balls = 0;

	for (int i = 0; i < n; ++i)
	{
		levels++;
		balls += levels;

		if (balls == n)
			return levels;

		if (balls > n)
			return levels - 1;
	}
}
*/

int pyramid(int n)
{
	int levels = 0;

	while (levels <= n)
	{
		n -= levels;
		levels++;
	}
	return levels - 1;
}
