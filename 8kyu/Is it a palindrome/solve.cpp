#include <string>
#include <algorithm>

/*
bool isPalindrom(const std::string& str)
{
	std::string s = str;
	std::transform(s.begin(), s.end(), s.begin(), ::tolower);

	int leftPos = 0;
	int rightPos = s.size() - 1;

	while (leftPos < rightPos)
	{
		if (s.at(leftPos) != s.at(rightPos))
			return false;

		leftPos++;
		rightPos--;
	}

	return true;
}
*/

/*
bool isPalindrom(const std::string& str)
{
	std::string s = str;

	std::transform(s.begin(), s.end(), s.begin(), ::tolower);

	return s == std::string(s.rbegin(), s.rend());
}
*/

/*
bool isPalindrom(const std::string& str)
{
	std::string lstr = str;

	for (char& c : lstr)
	{
		c = toupper(c);
	}

	return lstr == std::string(lstr.rbegin(), lstr.rend());
}
*/

bool isPalindrom(const std::string& str)
{
	auto leftPos = str.begin();
	auto rightPos = str.end() - 1;

	while (leftPos < rightPos)
	{
		if (tolower(*leftPos) != tolower(*rightPos))
			return false;

		++leftPos;
		--rightPos;
	}

	return true;
}
