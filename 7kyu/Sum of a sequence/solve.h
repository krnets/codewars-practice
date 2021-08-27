#pragma once

/*
int sequenceSum(int start, int end, int step)
{
	int sum = 0;

	for (int i = start; i <= end; i += step)
	{
		sum += i;
	}

	return sum;
}
*/


/*
int sequenceSum(int start, int end, int step)
{
	int sum = 0;

	while (start <= end)
	{
		sum += start;
		start += step;
	}

	return sum;
}
*/

int sequenceSum(int start, int end, int step)
{
	if (start > end)
		return 0;

	return start + sequenceSum(start + step, end, step);
}
