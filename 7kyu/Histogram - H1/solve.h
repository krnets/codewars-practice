#pragma once

std::string histogram(std::vector<int> results)
{
	std::ostringstream ans;
	int n = results.size();

	for (int i = n - 1; i >= 0; --i)
	{
		ans << i + 1;
		ans << '|';

		if (results[i] > 0)
		{
			ans << std::string(results[i], '#');
			ans << ' ';
			ans << results[i];
		}
		ans << '\n';
	}

	return ans.str();
}
