#pragma once

std::string capitalize(std::string s, std::vector<int> idxs)
{
	for (int i : idxs)
		if (i < s.length())
			s[i] = toupper(s[i]);

	return s;
}
