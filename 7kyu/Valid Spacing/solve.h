#pragma once

/*
bool valid_spacing(const std::string& s)
{
	if (s.front() == ' ' || s.back() == ' ')
		return false;

	for (int i = 0; i < s.length(); ++i)
		if (s.substr(i, 2) == "  ")
			return false;

	return true;
}
*/

bool valid_spacing(const std::string& s)
{
	return s.empty() ||
		s.front() != ' ' && s.back() != ' ' && s.find("  ") == std::string::npos;
}
