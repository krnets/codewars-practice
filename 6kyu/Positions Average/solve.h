#pragma once

using std::string;

double posAverage(const string& s)
{
	std::vector<string> nums;
	std::istringstream iss(s);
	string token;

	while (iss >> token)
		nums.push_back(token);

	int n = nums.size(), length = token.length();
	double numerator = 0, denominator = 0;

	for (int i = 0; i < n - 1; ++i)
	{
		for (int j = i + 1; j < n; ++j)
		{
			for (int k = 0; k < length; ++k)
			{
				if (nums[i][k] == nums[j][k])
					++numerator;

				++denominator;
			}
		}
	}
	return 100 * numerator / denominator;
}
