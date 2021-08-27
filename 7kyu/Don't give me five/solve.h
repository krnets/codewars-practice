#pragma once

/*
int dontGiveMeFive(int start, int end)
{
	int count = 0;

	for (int i = start; i <= end; ++i)
		if (std::to_string(i).find('5') == std::string::npos)
			count++;

	return count;
}
*/

/*
bool containsFive(int i)
{
	if (i == 0) return false;

	if (i % 5 == 0)
		if (i % 10 != 0)
			return true;

	return containsFive(i / 10);
};
*/

bool containsFive(int n)
{
	while (n > 0)
	{
		if (n % 10 == 5)
			return true;

		n /= 10;
	}

	return false;
};

int dontGiveMeFive(int start, int end)
{
	int count = 0;

	for (int i = start; i <= end; ++i)
		if (!containsFive(abs(i)))
			++count;

	return count;
}
