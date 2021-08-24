#pragma once
#include <string>

/*
class TwoToOne
{
public:
	static std::string longest(const std::string& s1, const std::string& s2);
};

inline std::string TwoToOne::longest(const std::string& s1, const std::string& s2)
{
	auto combined = s1 + s2;
	std::set<char> set(combined.begin(), combined.end());
	std::vector<char> v;
	v.reserve(set.size());

	for (char c : set)
		v.push_back(c);

	std::sort(v.begin(), v.end());

	return std::string(v.begin(), v.end());
}
*/

class TwoToOne
{
public:
	static std::string longest(const std::string& s1, const std::string& s2)
	{
		std::set<char> unique_chars(s1.begin(), s1.end());
		unique_chars.insert(s2.begin(), s2.end());

		return std::string(unique_chars.begin(), unique_chars.end());
	}
};
