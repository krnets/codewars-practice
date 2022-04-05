#pragma once

#include <vector>
#include <string>

std::vector<int> solve(const std::vector<std::string>& arr)
{
	std::vector<int> v;
	v.reserve(arr.size());

	for (const auto& str : arr)
	{
		int count = 0;

		for (int i = 0; i < str.length(); ++i)
		{
			if (::tolower(str[i]) == 'a' + i)
			{
				count++;
			}
		}

		v.push_back(count);
	}

	return v;
};
