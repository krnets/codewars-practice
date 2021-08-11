/*
#include <string>

int string_to_number(const std::string& s)
{
	return std::stoi(s);
}
*/


#include <string>

int string_to_number(const std::string& s)
{
	int n = 0;
	int i = s.size() - 1;
	int j = 1;
	bool negative = s[0] == '-';
	int stop = negative ? 1 : 0;

	while (i >= stop)
	{
		int x = s[i] - '0';

		n += x * j;

		--i;
		j *= 10;
	}

	return negative ? -n : n;
}
