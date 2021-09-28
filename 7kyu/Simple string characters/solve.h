#pragma once

std::vector<int> solve(std::string s)
{
	int upper_count = 0, lower_count = 0, numbers_count = 0, special_count = 0;

	for (char c : s)
		if (isupper(c)) upper_count++;
		else if (islower(c)) lower_count++;
		else if (isalnum(c)) numbers_count++;
		else special_count++;

	return {upper_count, lower_count, numbers_count, special_count};
}
