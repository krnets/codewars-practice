#pragma once

std::string solve(std::string s)
{
	auto left = s.begin();
	auto right = s.end() - 1;

	while (left < right)
	{
		if (isalpha(*left))
		{
			if (isalpha(*right))
			{
				std::swap(*left, *right);
				++left;
			}
			--right;
		}
		else ++left;
	}

	return s;
}
