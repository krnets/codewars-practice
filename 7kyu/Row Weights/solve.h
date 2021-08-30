#pragma once

#include <utility>

std::pair<int, int> rowWeights(const std::vector<int>& weights)
{
	std::pair<int, int> rows{0, 0};

	for (int i = 0; i < weights.size(); ++i)
	{
		if (i % 2 == 0)
			rows.first += weights[i];
		else
			rows.second += weights[i];
	}

	return rows;
}
