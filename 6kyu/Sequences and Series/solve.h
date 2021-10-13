#pragma once

/*
int getScore(int n)
{
	int score = 0, i = 0, inc = 50;

	while (i < n)
	{
		score += inc;
		inc += 50;
		++i;
	}
	return score;
}
*/

/*
int getScore(int n)
{
	return 50 * n * (n + 1) / 2;
}
*/

int getScore(int n)
{
	return 25 * n * (n + 1);
}
