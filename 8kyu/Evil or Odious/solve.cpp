#include <string>

std::string evil(int n)
{
	std::string o = "It's Odious!";
	std::string e = "It's Evil!";

	int count1s = 0;

	while (n != 0)
	{
		if ((n & 1) == 1)
			count1s++;

		n = n >> 1;
	}

	return count1s % 2 == 0 ? e : o;
}
