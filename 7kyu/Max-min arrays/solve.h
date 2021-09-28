#pragma once

std::vector<int> solve(std::vector<int> v)
{
	std::sort(v.begin(), v.end());
	std::vector<int> ans;

	for (int i = 0; v.size() > 0; ++i)
	{
		if (i % 2 == 0)
		{
			ans.push_back(v.back());
			v.pop_back();
		}
		else
		{
			ans.push_back(v.front());
			v.erase(v.begin(), v.begin() + 1);
		}
	}

	return ans;
}
