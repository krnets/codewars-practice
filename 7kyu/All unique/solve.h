#pragma once

/*
bool hasUniqueChars(std::string s)
{
	int freq_count[128] = {0};

	for (char c : s)
	{
		freq_count[c]++;

		if (freq_count[c] == 2)
			return false;
	}

	return true;
}
*/

bool hasUniqueChars(std::string s)
{
	const std::set unique(s.begin(), s.end());

	return unique.size() == s.length();
}
