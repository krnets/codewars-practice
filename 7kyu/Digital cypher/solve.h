#pragma once

class Kata
{
public:
	static std::vector<int> Encode(std::string str, int n)
	{
		std::vector<int> ans, nums;

		while (n > 0)
		{
			nums.push_back(n % 10);
			n /= 10;
		}

		int m = nums.size();

		for (int i = 0; i < str.length(); ++i)
		{
			ans.push_back(str[i] - 'a' + nums[m - 1 - i % m] + 1);
		}

		return ans;
	}
};
