#pragma once

#include <vector>

int save(std::vector<int> sizes, int hd)
{
	int count = 0, sum = 0;

	for (int chunk : sizes)
	{
		sum += chunk;

		if (sum > hd)
			break;

		count++;
	}

	return count;
}
