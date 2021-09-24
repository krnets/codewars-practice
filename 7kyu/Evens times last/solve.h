#pragma once

#include <vector>

int even_last(std::vector<int> nums)
{
	int sum = 0;

	for (int i = 0; i < nums.size(); i += 2)
	{
		sum += nums[i];
	}
	return nums.empty() ? 0 : sum * nums.back();
}
