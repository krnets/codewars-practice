#pragma once

std::vector<int> bubbleSortOnce(const std::vector<int>& input)
{
	std::vector vec(input);

	for (size_t i = 1; i < vec.size(); ++i)
		if (vec[i - 1] > vec[i])
			std::swap(vec[i - 1], vec[i]);

	return vec;
}
