#pragma once

/*
bool is_happy(unsigned short n)
{
	std::string n_str = std::to_string(n);
	std::set n_set(n_str.begin(), n_str.end());

	return n_set.size() == n_str.length();
};

unsigned short int nextHappyYear(unsigned short int year)
{
	unsigned short ans = year + 1;

	while (!is_happy(ans))
		++ans;

	return ans;
}
*/

unsigned short int nextHappyYear(unsigned short int year)
{
	std::string s;

	do
	{
		++year;
		s = std::to_string(year);
	}
	while (s.length() != std::set(s.begin(), s.end()).size());

	return year;
}
