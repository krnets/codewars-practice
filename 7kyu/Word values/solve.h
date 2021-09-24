#pragma once


std::vector<int> wordValue(std::vector<std::string> arr)
{
	std::vector<int> v;

	for (size_t i = 0; i < arr.size(); ++i)
	{
		int sum = 0;

		for (char c : arr[i])
			if (isalnum(c))
				sum += (c - 'a' + 1);

		v.push_back(sum * (i + 1));
	}

	return v;
}

