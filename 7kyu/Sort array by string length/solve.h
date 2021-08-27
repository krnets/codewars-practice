#pragma once

class Kata
{
public:
	std::vector<std::string> sortByLength(std::vector<std::string> array)
	{
		auto keyByLength = [](std::string& s, std::string& t) { return s.length() < t.length(); };
		std::sort(array.begin(), array.end(), keyByLength);

		return array;
	}
};
