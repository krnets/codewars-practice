#pragma once

bool small_enough(std::vector<int> arr, int limit)
{
	return std::none_of(arr.begin(), arr.end(), [limit](int x) { return x > limit; });
}
