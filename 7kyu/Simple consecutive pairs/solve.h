#pragma once

int pairs(std::vector<int> arr)
{
	int count = 0;

	for (int i = 0; i < arr.size() - 1; i += 2)
		if (abs(arr[i] - arr[i + 1]) == 1)
			count++;

	return count;
}
