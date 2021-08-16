#include <string>
#include <algorithm>

/*
bool is_uppercase(const std::string& s)
{
	for (char c : s)
		if (c >= 'a' && c <= 'z')
			return false;

	return true;
}
*/


bool is_uppercase(const std::string& s)
{
	return none_of(s.begin(), s.end(), islower);
}
