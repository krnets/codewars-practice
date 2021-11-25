#pragma once

using std::string;

unsigned solve(const string& s, unsigned k)
{
	std::vector<string> nums;
	std::istringstream iss(s);
	string token;

	while (iss >> token)
		nums.push_back(token);

	int count = 0, n = nums.size();

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			if (i == j)
				continue;

			if (stoi(nums[i] + nums[j]) % k == 0)
				++count;
		}
	}
	return count;
}
